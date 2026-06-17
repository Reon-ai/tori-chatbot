"""
backend/app/services/rag_service.py
Core RAG pipeline:
  1. Preprocess query
  2. Embed query
  3. Semantic search → top-k chunks
  4. Re-rank (MMR / simple score filter)
  5. Build context + conversation history
  6. Call OpenAI ChatCompletion
  7. Return clean response (no source citations)
"""

from __future__ import annotations

import asyncio
import time
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI, APIError, RateLimitError

from app.utils.logger import logger
from app.utils.config import get_settings
from app.services.vector_store import get_vector_store, SearchResult
from app.services.database import get_db
from app.services.intent_detector import get_intent_detector


class RAGService:
    """Retrieval-Augmented Generation pipeline."""

    def __init__(self) -> None:
        self.settings       = get_settings()
        self.vector_store   = get_vector_store()
        self.db             = get_db()
        self.intent_detector = get_intent_detector()
        self._openai_client: Optional[AsyncOpenAI] = None

    @property
    def openai_client(self) -> AsyncOpenAI:
        if self._openai_client is None:
            if not self.settings.openai_api_key:
                raise ValueError(
                    "OPENAI_API_KEY is not configured. "
                    "Add it to your .env file and restart the server."
                )
            self._openai_client = AsyncOpenAI(api_key=self.settings.openai_api_key)
        return self._openai_client

    # ══════════════════════════════════════════════════════════════
    # PUBLIC: generate_response
    # ══════════════════════════════════════════════════════════════
    async def generate_response(
        self,
        session_id: str,
        user_message: str,
    ) -> Dict[str, Any]:
        """
        Full RAG pipeline execution.
        Checks for form-triggering intents FIRST, then falls back to RAG.
        Returns dict with 'response', 'processing_ms', 'retrieved_chunks'.
        May include 'type' and 'form_id' when a form intent is detected.
        """
        start_ms = int(time.time() * 1000)

        try:
            # ── STEP 0: Intent Detection ─────────────────────────
            intent_result = self.intent_detector.detect(user_message)
            if intent_result:
                form_id = intent_result["form_id"]
                form_message = self.intent_detector.get_form_message(form_id)
                elapsed = int(time.time() * 1000) - start_ms

                logger.info(
                    f"FORM_TRIGGER | session={session_id[:8]} | "
                    f"intent={intent_result['intent']} | "
                    f"form={form_id} | conf={intent_result['confidence']} | "
                    f"{elapsed}ms"
                )

                return {
                    "response":         form_message,
                    "type":             "form",
                    "form_id":          form_id,
                    "processing_ms":    elapsed,
                    "retrieved_chunks": [],
                }

            # ── STEPS 1–7: Standard RAG Pipeline ─────────────────
            clean_query = self._preprocess_query(user_message)

            query_embedding = await self._embed_query(clean_query)

            results = await self.vector_store.search(
                query_embedding=query_embedding,
                top_k=self.settings.top_k,
            )

            filtered = self._rerank(results, self.settings.similarity_threshold)

            context = self._build_context(filtered)

            history = await self.db.get_session_history(
                session_id, limit=self.settings.memory_turns
            )
            history_text = self._format_history(history)

            response_text = await self._call_llm(
                user_query=clean_query,
                context=context,
                history=history_text,
            )

            elapsed = int(time.time() * 1000) - start_ms
            chunk_ids = [r.chunk_id for r in filtered]

            logger.info(
                f"RAG | session={session_id[:8]} | "
                f"query='{clean_query[:60]}' | "
                f"chunks={len(filtered)} | {elapsed}ms"
            )

            return {
                "response":         response_text,
                "type":             "text",
                "processing_ms":    elapsed,
                "retrieved_chunks": chunk_ids,
            }

        except ValueError as e:
            logger.error(f"RAG config error: {e}")
            return {
                "response": (
                    "I'm sorry, the assistant isn't fully configured yet. "
                    "Please contact support if this persists."
                ),
                "type": "text",
                "processing_ms": int(time.time() * 1000) - start_ms,
                "retrieved_chunks": [],
            }
        except Exception as e:
            logger.error(f"RAG pipeline error: {e}", exc_info=True)
            return {
                "response": (
                    "I apologize, I'm having trouble processing your request right now. "
                    "Please try again in a moment, or contact our support team for immediate help."
                ),
                "type": "text",
                "processing_ms": int(time.time() * 1000) - start_ms,
                "retrieved_chunks": [],
            }

    # ══════════════════════════════════════════════════════════════
    # STEP 1: Preprocess query
    # ══════════════════════════════════════════════════════════════
    def _preprocess_query(self, query: str) -> str:
        """
        Clean and normalise the user query.
        - Strip whitespace
        - Collapse multiple spaces
        - Limit length to avoid token waste
        """
        cleaned = " ".join(query.split())
        if len(cleaned) > 1000:
            cleaned = cleaned[:1000] + "…"
        return cleaned

    # ══════════════════════════════════════════════════════════════
    # STEP 2: Embed query
    # ══════════════════════════════════════════════════════════════
    async def _embed_query(self, query: str) -> List[float]:
        for attempt in range(3):
            try:
                resp = await self.openai_client.embeddings.create(
                    model=self.settings.openai_embedding_model,
                    input=query,
                )
                return resp.data[0].embedding
            except RateLimitError:
                wait = 2 ** attempt
                logger.warning(f"Embedding rate limited, retrying in {wait}s…")
                await asyncio.sleep(wait)
            except Exception as e:
                if attempt == 2:
                    raise
                await asyncio.sleep(1)

    # ══════════════════════════════════════════════════════════════
    # STEP 3+4: Retrieve + Re-rank
    # ══════════════════════════════════════════════════════════════
    def _rerank(
        self,
        results: List[SearchResult],
        threshold: float,
    ) -> List[SearchResult]:
        """
        Filter by similarity threshold and apply simple Maximal Marginal Relevance
        to reduce redundancy between top results.
        """
        filtered = [r for r in results if r.score >= threshold]

        if not filtered:
            if results:
                logger.info("No results above threshold; using best available match")
                return [results[0]]
            return []

        if len(filtered) <= 2:
            return filtered

        selected   = [filtered[0]]
        remaining  = filtered[1:]

        while remaining and len(selected) < self.settings.top_k:
            best     = None
            best_val = -1

            for cand in remaining:
                max_overlap = max(
                    self._text_overlap(cand.text, sel.text) for sel in selected
                )
                mmr_score = cand.score - 0.3 * max_overlap
                if mmr_score > best_val:
                    best_val = mmr_score
                    best     = cand

            if best:
                selected.append(best)
                remaining.remove(best)

        return selected

    @staticmethod
    def _text_overlap(a: str, b: str) -> float:
        """Simple Jaccard-like word overlap metric."""
        words_a = set(a.lower().split())
        words_b = set(b.lower().split())
        if not words_a or not words_b:
            return 0.0
        inter = words_a & words_b
        union = words_a | words_b
        return len(inter) / len(union)

    # ══════════════════════════════════════════════════════════════
    # STEP 5: Build context
    # ══════════════════════════════════════════════════════════════
    def _build_context(self, results: List[SearchResult]) -> str:
        if not results:
            return "No specific information found in the knowledge base."

        parts = []
        for i, r in enumerate(results, 1):
            parts.append(f"[Context {i}]\n{r.text.strip()}")

        return "\n\n".join(parts)

    def _format_history(self, history: List[Dict]) -> str:
        if not history:
            return "No previous conversation."

        lines = []
        for turn in history:
            lines.append(f"Customer: {turn['user_message']}")
            lines.append(f"Assistant: {turn['bot_response']}")

        return "\n".join(lines)

    # ══════════════════════════════════════════════════════════════
    # STEP 6: LLM call
    # ══════════════════════════════════════════════════════════════
    async def _call_llm(
        self,
        user_query: str,
        context: str,
        history: str,
    ) -> str:
        """
        Build the chat prompt and call OpenAI ChatCompletion API.
        Includes retry logic for transient errors.
        """
        model       = await self.db.get_config("model",       self.settings.openai_chat_model)
        temperature = await self.db.get_config("temperature", self.settings.openai_temperature)
        max_tokens  = await self.db.get_config("max_tokens",  self.settings.openai_max_tokens)
        sys_prompt  = await self.db.get_config("system_prompt", self.settings.system_prompt)
        biz_name    = await self.db.get_config("business_name", self.settings.business_name)

        system_content = sys_prompt.format(
            business_name=biz_name,
            retrieved_context=context,
            conversation_history=history,
            user_query=user_query,
        )

        messages = [
            {"role": "system",    "content": system_content},
            {"role": "user",      "content": user_query},
        ]

        for attempt in range(3):
            try:
                resp = await self.openai_client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=float(temperature),
                    max_tokens=int(max_tokens),
                    stream=False,
                )
                return resp.choices[0].message.content.strip()

            except RateLimitError:
                wait = 2 ** attempt
                logger.warning(f"LLM rate limited, retrying in {wait}s…")
                await asyncio.sleep(wait)

            except APIError as e:
                if e.status_code in (500, 502, 503) and attempt < 2:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise

        raise RuntimeError("LLM call failed after 3 attempts")

    # ══════════════════════════════════════════════════════════════
    # HEALTH CHECK
    # ══════════════════════════════════════════════════════════════
    async def check_openai(self) -> bool:
        """Verify OpenAI API key is valid."""
        try:
            await self.openai_client.models.list()
            return True
        except Exception:
            return False


# Singleton
_rag_service: Optional[RAGService] = None


def get_rag_service() -> RAGService:
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service