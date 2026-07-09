"""
backend/app/services/rag_service.py
Core RAG pipeline:
  1. Preprocess query
  2. Embed query
  3. Semantic search → top-k chunks
  4. Re-rank (MMR / simple score filter)
  5. Build context + conversation history
  6. Call OpenAI ChatCompletion
  7. Deterministic intent → structured form_action injected into response
  8. Return clean response + optional form_action
"""

from __future__ import annotations

import asyncio
import re
import time
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI, APIError, RateLimitError

from app.utils.logger import logger
from app.utils.config import get_settings
from app.services.vector_store import get_vector_store, SearchResult
from app.services.database import get_db


# ══════════════════════════════════════════════════════════════════
# DETERMINISTIC FORM TRIGGER
#
# Maps user intent patterns → structured form actions.
# Each tuple: (compiled_regex, formId, bridge_message)
#
# The bridge_message is the conversational sentence the bot says
# BEFORE presenting the form — it reads naturally in chat.
#
# formId must match a file in /forms/<formId>_form.json
# ══════════════════════════════════════════════════════════════════

_TRIGGER_PATTERNS = [
    # ── Quote / pricing ───────────────────────────────────────────
    (
        re.compile(r'\bquotes?\b|\bquotation\b|\bkwotasie\b|\bkwot\b', re.I),
        'tile_quote',
        'Absolutely — please complete the quick form below and a consultant will prepare an accurate quote for you.',
    ),
    (
        # SOFT / continuation-sensitive — see _CONTINUATION_SENSITIVE_FORM_IDS below.
        # "How much" is ambiguous: it can mean "how much does it cost" (new lead)
        # OR "how much adhesive/grout do I need" (a calculation follow-up that
        # should just be answered, not redirected to a form).
        re.compile(r'\bhow\s+much\b|\bwhat.{0,20}(cost|price|pricing)\b|\bwat\s+kos\b|\bhoeveel\s+kos\b|\bhoeveel\b|\bpryse?\b', re.I),
        'tile_quote',
        'Great question. To give you an accurate price, I need a few details — please complete the short form below.',
    ),
    (
        re.compile(r'\b(get|send|give|need|want|require|request)\s+.{0,15}quote\b', re.I),
        'tile_quote',
        'Of course! Please fill in the form below and our team will get back to you with a quote.',
    ),
    (
        re.compile(r'\bi\s+want\s+to\s+(buy|order|purchase)\b|\bready\s+to\s+(buy|order)\b|\bplace\s+an?\s+order\b|\bgo\s+ahead\b|\bkoop\b|\bbestel\b', re.I),
        'tile_quote',
        "That's great news! Please complete the form below so our team can assist you with your order.",
    ),

    # ── Contact / call / WhatsApp ─────────────────────────────────
    (
        re.compile(r'\b(call|phone|ring)\s+me\b|\bgive\s+me\s+a\s+call\b|\bbel\s+my\b|\bskakel\s+my\b', re.I),
        'contact_me',
        'Sure! Leave your details below and a consultant will call you back.',
    ),
    (
        re.compile(r'\bcontact\s+me\b|\bget\s+back\s+to\s+me\b|\breach\s+out\b|\bkontak\s+my\b', re.I),
        'contact_me',
        'No problem — fill in your details below and we will be in touch shortly.',
    ),
    (
        re.compile(r'\b(can|could|would|may|please)\s+(someone|anyone|a\s+person|a\s+consultant)\b', re.I),
        'contact_me',
        'Of course! Please leave your details and one of our consultants will contact you.',
    ),
    (
        re.compile(r'\bwhatsapp\s+me\b|\bwa\s+me\b|\bsend.{0,10}whatsapp\b', re.I),
        'contact_me',
        "Absolutely — pop your details in below and we'll WhatsApp you right back.",
    ),
    (
        re.compile(r'\bspeak\s+to\s+(a\s+)?(person|human|consultant|someone)\b|\btalk\s+to\s+(a\s+)?(person|human|consultant|someone)\b', re.I),
        'contact_me',
        'Happy to connect you with a consultant. Please fill in the form below and they will be in touch.',
    ),
    (
        re.compile(r'\bkan\s+iemand\b|\biemand.{0,20}(bel|kontak|help)\b', re.I),
        'contact_me',
        "Geen probleem! Laat jou besonderhede hieronder en 'n konsultant sal jou skakel.",
    ),

    # ── Trade / contractor ────────────────────────────────────────
    (
        re.compile(r'\bcontractor\b|\bbuilder\b|\btrade\s*(price|account|discount)?\b|\bbulk\s*(order|buy)?\b|\barchitect\b|\binterior\s+design\w*\b|\bcommercial\s+project\b', re.I),
        'contractor_quote',
        'Great — we love working with trade professionals. Please complete the trade form below for dedicated pricing and support.',
    ),

    # ── Showroom / store visit ────────────────────────────────────
    (
        re.compile(r'\bbook\s+an?\s+appointment\b|\bvisit\s+the\s+showroom\b|\bcome\s+in\b|\bshowroom\s+appointment\b', re.I),
        'store_assistance',
        'We would love to see you! Please complete the booking form below and we will confirm your appointment.',
    ),

    # ── Product advice ────────────────────────────────────────────
    (
        re.compile(r'\bwhich\s+(tile|product|grout|adhesive)\b|\bwhat\s+(tile|product)\s+(should|do)\b|\bhelp\s+me\s+choose\b|\brecommend\s+(a\s+)?(tile|product)\b', re.I),
        'product_enquiry',
        'I would love to help you find the right product. Please share a few more details using the form below.',
    ),

    # ── Sample request ────────────────────────────────────────────
    (
        re.compile(r'\bsample\b|\bsee\s+the\s+(tile|product)\b|\bbring\s+a\s+sample\b|\bview\s+in\s+(my\s+)?home\b', re.I),
        'sample_request',
        'Seeing is believing! Please fill in the form below and we will arrange samples for you.',
    ),

    # ── Stock / availability ──────────────────────────────────────
    (
        re.compile(r'\bin\s+stock\b|\bdo\s+you\s+(have|stock|carry)\b|\bstock\s+(available|check)\b|\bavailabilit\w+\b|\bstill\s+available\b', re.I),
        'product_enquiry',
        'I can check that for you. Please give us your details in the form below and we will confirm stock.',
    ),

    # ── Delivery ──────────────────────────────────────────────────
    (
        re.compile(r'\bdeliver\w*\b|\bshipping\b|\bdo\s+you\s+deliver\b|\bdelivery\s+(cost|fee|time)\b', re.I),
        'contact_me',
        'We can arrange delivery to your door. Leave your details below and we will confirm costs and timing.',
    ),

    # ── Tile calculation ──────────────────────────────────────────
    (
        re.compile(r'\bhow\s+many\s+tiles?\b|\bhow\s+many\s+boxes\b|\bcalculate.{0,20}(tiles?|quantities?)\b|\b\d+\s*(m²|m2|sqm)\b', re.I),
        'tile_quote',
        'I can help calculate what you need. Please fill in your details and measurements below.',
    ),
]


# ══════════════════════════════════════════════════════════════════
# CALCULATION CONTINUITY GUARD
#
# Some trigger patterns (e.g. "how much", "how many tiles") are ambiguous:
# they can mean "what does this cost" (a genuine new lead) OR they can be
# a natural follow-up question inside a calculation the bot itself already
# started (e.g. "how much adhesive and grout do I need?" right after the
# bot gave a tile count). Firing the lead form in the second case hijacks
# a conversation the bot is fully capable of finishing itself, and feels
# broken to the customer.
#
# To fix this without losing the deterministic safety net for genuinely
# new pricing/quote requests, we look at the recent conversation history:
# if the assistant has recently been doing tile/area/quantity math, we
# suppress the *ambiguous* quantity/price patterns and let the LLM keep
# calculating (per the CALCULATIONS RULE in the system prompt). Patterns
# that are NOT ambiguous (explicit "quote", "order", "call me", etc.)
# still fire immediately regardless of calculation context.
# ══════════════════════════════════════════════════════════════════

# formIds that are safe to suppress mid-calculation (only the calculation-
# ambiguous ones — NOT contact/order/complaint patterns, which should
# always fire immediately).
_CONTINUATION_SENSITIVE_PATTERN_INDEXES = {1, 12}  # "how much..." and "tile calculation" patterns

_CALCULATION_CONTEXT_RE = re.compile(
    r'\bm²|m2|sqm\b|\btiles?\b|\bboxes?\b|\badhesive\b|\bgrout\b|\bcoverage\b|'
    r'\bbags?\b|\btrowel\b|\bback[- ]butter\w*\b|\bwaste\b|\bsubstrate\b|\bpack\s*size\b',
    re.I,
)


def _is_mid_calculation(history_text: str) -> bool:
    """
    Heuristic: has the assistant been discussing tile/adhesive/grout
    quantities in the last few turns of this session? Only looks at the
    recent history text already fetched for this turn (memory_turns-limited).
    """
    if not history_text or history_text == "No previous conversation.":
        return False
    return bool(_CALCULATION_CONTEXT_RE.search(history_text))


def _should_trigger_form(
    user_message: str,
    history_text: str = "",
) -> Optional[Dict[str, str]]:
    """
    Returns a form_action dict if the user message matches a trigger pattern.
    Returns None if no trigger is found.

    The returned dict has:
        formId   — matches a /forms/<formId>_form.json file
        message  — conversational bridge sentence to show before the form

    `history_text` (recent conversation) is used to avoid interrupting an
    in-progress tile/adhesive/grout calculation with the lead form — see
    CALCULATION CONTINUITY GUARD above.
    """
    mid_calc = _is_mid_calculation(history_text)

    for idx, (pattern, form_id, message) in enumerate(_TRIGGER_PATTERNS):
        if not pattern.search(user_message):
            continue
        if mid_calc and idx in _CONTINUATION_SENSITIVE_PATTERN_INDEXES:
            # Let the LLM keep calculating instead of jumping to the form.
            continue
        return {"formId": form_id, "message": message}
    return None


class RAGService:
    """Retrieval-Augmented Generation pipeline."""

    def __init__(self) -> None:
        self.settings     = get_settings()
        self.vector_store = get_vector_store()
        self.db           = get_db()
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
        Returns dict with 'response', 'processing_ms', 'retrieved_chunks'.
        """
        start_ms = int(time.time() * 1000)

        try:
            # 1. Preprocess query
            clean_query = self._preprocess_query(user_message)

            # 2. Embed query
            query_embedding = await self._embed_query(clean_query)

            # 3. Retrieve context
            results = await self.vector_store.search(
                query_embedding=query_embedding,
                top_k=self.settings.top_k,
            )

            # 4. Filter by similarity threshold & re-rank
            filtered = self._rerank(results, self.settings.similarity_threshold)

            # 5. Build context string
            context = self._build_context(filtered)

            # 6. Get conversation history
            history = await self.db.get_session_history(
                session_id, limit=self.settings.memory_turns
            )
            history_text = self._format_history(history)

            # 7. Call LLM
            response_text = await self._call_llm(
                user_query=clean_query,
                context=context,
                history=history_text,
            )

            elapsed = int(time.time() * 1000) - start_ms
            chunk_ids = [r.chunk_id for r in filtered]

            # 8. Deterministic form trigger — independent of LLM output
            # Checks the raw user message against intent patterns.
            # Returns a structured form_action if triggered.
            form_action = _should_trigger_form(user_message, history_text)
            if form_action:
                logger.info(
                    f"FORM TRIGGER | session={session_id[:8]} | "
                    f"formId='{form_action['formId']}' | query='{clean_query[:60]}'"
                )
            elif _is_mid_calculation(history_text):
                logger.info(
                    f"FORM TRIGGER SUPPRESSED (mid-calculation) | session={session_id[:8]} | "
                    f"query='{clean_query[:60]}'"
                )

            logger.info(
                f"RAG | session={session_id[:8]} | "
                f"query='{clean_query[:60]}' | "
                f"chunks={len(filtered)} | {elapsed}ms"
            )

            return {
                "response":         response_text,
                "form_action":      form_action,   # None or {"formId": ..., "message": ...}
                "processing_ms":    elapsed,
                "retrieved_chunks": chunk_ids,
            }

        except ValueError as e:
            # Config issues (missing API key, etc.)
            logger.error(f"RAG config error: {e}")
            return {
                "response": (
                    "Hi, I'm Tori from Tiletoria. It looks like I'm not fully set up just yet. "
                    "Please contact our team at your nearest Tiletoria showroom and we'll assist you directly."
                ),
                "form_action":   None,
                "processing_ms": int(time.time() * 1000) - start_ms,
                "retrieved_chunks": [],
            }
        except Exception as e:
            logger.error(f"RAG pipeline error: {e}", exc_info=True)
            return {
                "response": (
                    "Apologies — I'm having a little trouble on my end right now. "
                    "Please try again in a moment, or visit your nearest Tiletoria showroom and our team will be happy to help."
                ),
                "form_action":   None,
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
        # Filter by threshold
        filtered = [r for r in results if r.score >= threshold]

        if not filtered:
            # Graceful degradation: return top-1 even if below threshold
            if results:
                logger.info("No results above threshold; using best available match")
                return [results[0]]
            return []

        # MMR: greedily pick diverse results
        if len(filtered) <= 2:
            return filtered

        selected   = [filtered[0]]
        remaining  = filtered[1:]

        while remaining and len(selected) < self.settings.top_k:
            # Score = relevance (score) - max similarity to already selected
            best     = None
            best_val = -1

            for cand in remaining:
                # Rough text overlap as a diversity metric
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
        # Retrieve current config (may have been updated via admin panel)
        model       = await self.db.get_config("model",       self.settings.openai_chat_model)
        temperature = await self.db.get_config("temperature", self.settings.openai_temperature)
        max_tokens  = await self.db.get_config("max_tokens",  self.settings.openai_max_tokens)
        sys_prompt  = await self.db.get_config("system_prompt", self.settings.system_prompt)
        biz_name    = await self.db.get_config("business_name", self.settings.business_name)

        # Fill in template variables
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
