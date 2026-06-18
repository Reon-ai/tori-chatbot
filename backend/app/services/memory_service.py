"""
backend/app/services/memory_service.py
Session memory system for Tori chatbot.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI

from app.utils.logger import logger
from app.utils.config import get_settings
from app.services.database import get_db, Database


DEFAULT_PROJECT_STATE: Dict[str, Any] = {
    "persona": None,
    "branch_region": None,
    "project_type": None,
    "application_area": None,
    "product_interest": None,
    "measured_area_m2": None,
    "waste_percent": None,
    "calculated_required_m2": None,
    "budget_level": None,
    "urgency": None,
    "needs_quote": False,
    "needs_live_stock_check": False,
    "needs_live_price_check": False,
    "complaint_or_escalation": False,
    "missing_fields": [],
}

DEFAULT_QUOTE_FORM: Dict[str, Any] = {
    "customer_name": None,
    "phone": None,
    "email": None,
    "preferred_branch": None,
    "customer_type": None,
    "project_type": None,
    "product_category": None,
    "area_m2": None,
    "required_m2_with_waste": None,
    "tile_size": None,
    "urgency": None,
    "delivery_or_collection": None,
    "notes": None,
    "consent_to_contact": False,
}

_SYSTEM_PROMPT_WITH_MEMORY = """You are Tori, an intelligent customer service assistant for {business_name}.

Your role:
- Answer questions about products, orders, shipping, returns, and policies using ONLY the provided knowledge base context
- Be helpful, friendly, and concise
- Present information naturally without referencing source documents
- If you don't know something, say so honestly

IMPORTANT MEMORY RULES:
- You have a conversation memory below. Use it to personalise responses.
- NEVER ask a question the customer already answered in this conversation.
- NEVER repeat questions. Only ask for MISSING information.
- If the customer gave you their area, room type, or product interest, remember it and use it.
- When a quote form is partially filled, acknowledge what you already know and only ask for what's missing.
- NEVER invent live business information: no live stock levels, no current prices, no delivery ETAs.
- If the customer asks about live stock or current prices you can't confirm, say: "I'll have the correct branch team confirm that for you."

## Knowledge Base Context
{retrieved_context}

## Conversation Memory
{memory_context}

## Current Customer Question
{user_query}

Respond naturally, conversationally, and helpfully. Use the customer's name and details if known. Keep responses under 200 words unless a detailed explanation is needed."""


class MemoryService:
    """Orchestrates session memory: message storage, summary generation, project state extraction, and form state tracking."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self.db = get_db()
        self._msg_counts: Dict[str, int] = {}

    async def save_message(self, session_id: str, role: str, message: str) -> None:
        """Store a single message (user or assistant)."""
        msg_id = str(uuid.uuid4())
        await self.db.save_conversation_message(msg_id, session_id, role, message)
        self._msg_counts[session_id] = self._msg_counts.get(session_id, 0) + 1

    async def get_recent_messages(self, session_id: str, limit: int = 12) -> List[Dict[str, Any]]:
        """Return the last N messages for a session."""
        return await self.db.get_conversation_messages(session_id, limit)

    async def maybe_update_memory(self, session_id: str, openai_client: AsyncOpenAI) -> None:
        """Regenerate summary and state if enough new messages have accumulated."""
        count = self._msg_counts.get(session_id, 0)
        interval = self.settings.memory_summary_interval
        if count < interval:
            return
        self._msg_counts[session_id] = 0
        await self._regenerate_summary_and_state(session_id, openai_client)

    async def build_memory_context(self, session_id: str) -> str:
        """Build the memory block that gets injected into the system prompt."""
        parts: List[str] = []

        # Summary
        summary_row = await self.db.get_conversation_summary(session_id)
        if summary_row:
            parts.append(f"Summary: {summary_row['summary']}")

        # Project state
        state_row = await self.db.get_conversation_state(session_id)
        if state_row:
            state = json.loads(state_row["state_json"])
            filled = []
            for key, val in state.items():
                if key == "missing_fields":
                    continue
                if val is not None and val is not False and val != []:
                    label = key.replace("_", " ").title()
                    filled.append(f"- {label}: {val}")
            if filled:
                parts.append("Project Details:\n" + "\n".join(filled))
            missing = state.get("missing_fields", [])
            if missing:
                parts.append(f"Still Need: {', '.join(missing)}")

        # Form state
        form_rows = await self.db.get_form_states(session_id)
        for form in form_rows:
            form_data = json.loads(form["form_json"])
            filled_fields = []
            empty_fields = []
            for k, v in form_data.items():
                if v is not None and v is not False and v != "":
                    filled_fields.append(f"  {k}: {v}")
                else:
                    empty_fields.append(f"  {k}: (empty)")
            if filled_fields or empty_fields:
                parts.append(f"Form: {form['form_type']} ({form['status']})\n" + "\n".join(filled_fields + empty_fields))

        # Recent messages (last 8)
        recent = await self.get_recent_messages(session_id, limit=8)
        if recent:
            msg_lines = []
            for m in recent:
                role_label = "Customer" if m["role"] == "user" else "Tori"
                msg_lines.append(f"{role_label}: {m['message']}")
            parts.append("Recent Conversation:\n" + "\n".join(msg_lines))

        return "\n\n".join(parts) if parts else "No previous conversation."

    def get_system_prompt_template(self) -> str:
        """Return the memory-aware system prompt template."""
        return _SYSTEM_PROMPT_WITH_MEMORY

    async def get_or_create_form_state(self, session_id: str, form_type: str) -> Dict[str, Any]:
        """Get existing form state or create a blank one."""
        existing = await self.db.get_form_state(session_id, form_type)
        if existing:
            return json.loads(existing["form_json"])
        blank = DEFAULT_QUOTE_FORM.copy()
        await self.db.save_form_state(session_id, form_type, blank, "in_progress")
        return blank

    async def update_form_state(self, session_id: str, form_type: str, data: Dict[str, Any], status: str = "in_progress") -> None:
        """Update form state with new data."""
        await self.db.save_form_state(session_id, form_type, data, status)

    async def _regenerate_summary_and_state(self, session_id: str, openai_client: AsyncOpenAI) -> None:
        """Fetch all messages, call LLM to extract summary + state, store results."""
        try:
            messages = await self.db.get_conversation_messages(session_id, limit=50)
            if len(messages) < 2:
                return
            lines = []
            for m in messages:
                role = "Customer" if m["role"] == "user" else "Assistant"
                lines.append(f"{role}: {m['message']}")
            conversation_text = "\n".join(lines)
            await self._extract_summary(session_id, conversation_text, openai_client)
            await self._extract_quote_form(session_id, conversation_text, openai_client)
            logger.info(f"Memory updated for session={session_id[:8]}")
        except Exception as e:
            logger.error(f"Memory update failed for session={session_id[:8]}: {e}")

    async def _extract_summary(self, session_id: str, conversation_text: str, openai_client: AsyncOpenAI) -> None:
        """Call LLM to extract summary and project state."""
        prompt = f"""You are a conversation analysis assistant for a South African tile retailer called Tiletoria.

Analyze the conversation below and extract key details.

Return ONLY a JSON object with this exact structure (no markdown, no explanation):

{{
  "summary": "2-3 sentence summary of what the customer wants and what we know",
  "persona": "homeowner | contractor | interior_designer | architect | builder | other | null",
  "branch_region": "specific branch name or city or null",
  "project_type": "bathroom | kitchen | living_room | bedroom | outdoor_patio | commercial | renovation | new_build | other | null",
  "application_area": "floor | wall | shower | backsplash | outdoor | countertop | other | null",
  "product_interest": "ceramic_tiles | porcelain_tiles | natural_stone | mosaic | vinyl | laminate | adhesive_grout | sanitaryware | accessories | other | null",
  "measured_area_m2": null,
  "waste_percent": null,
  "calculated_required_m2": null,
  "budget_level": "low | medium | high | luxury | null",
  "urgency": "asap | this_week | this_month | flexible | null",
  "needs_quote": false,
  "needs_live_stock_check": false,
  "needs_live_price_check": false,
  "complaint_or_escalation": false,
  "missing_fields": ["list", "of", "info", "we", "still", "need"]
}}

Rules:
- If the customer mentioned a measurement in m2, record it as a number.
- If they mentioned waste percentage or you can infer it (typically 10%), record it.
- If you can calculate required m2 (area + waste), record it.
- Only set needs_live_stock_check to true if the customer asks about current stock levels.
- Only set needs_live_price_check to true if the customer asks about current prices.
- missing_fields should list only what we genuinely don't know yet.

Conversation:
{conversation_text}

JSON output:"""

        resp = await openai_client.chat.completions.create(
            model=self.settings.openai_chat_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=800,
            response_format={"type": "json_object"},
        )
        raw = resp.choices[0].message.content.strip()
        extracted = json.loads(raw)

        summary = extracted.get("summary", "")
        await self.db.save_conversation_summary(session_id, summary)

        state = DEFAULT_PROJECT_STATE.copy()
        for key in state.keys():
            if key in extracted:
                state[key] = extracted[key]
        await self.db.save_conversation_state(session_id, state)

    async def _extract_quote_form(self, session_id: str, conversation_text: str, openai_client: AsyncOpenAI) -> None:
        """Call LLM to extract quote form fields from conversation."""
        prompt = f"""You are a form-filling assistant for Tiletoria, a South African tile retailer.

Analyze the conversation and extract any details that fill in a quote request form.

Return ONLY a JSON object with this exact structure (no markdown, no explanation):

{{
  "customer_name": null,
  "phone": null,
  "email": null,
  "preferred_branch": null,
  "customer_type": null,
  "project_type": null,
  "product_category": null,
  "area_m2": null,
  "required_m2_with_waste": null,
  "tile_size": null,
  "urgency": null,
  "delivery_or_collection": null,
  "notes": null,
  "consent_to_contact": false
}}

Rules:
- Only fill fields the customer explicitly provided or strongly implied.
- Do NOT guess or invent values.
- If the customer mentioned a phone number, email, or name anywhere in the conversation, capture it.
- area_m2 should be a number only (e.g. 18, not "18m2").
- required_m2_with_waste should be calculated if possible (area + 10% waste).
- consent_to_contact should only be true if the customer explicitly agreed to be contacted.

Conversation:
{conversation_text}

JSON output:"""

        resp = await openai_client.chat.completions.create(
            model=self.settings.openai_chat_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=600,
            response_format={"type": "json_object"},
        )
        raw = resp.choices[0].message.content.strip()
        extracted = json.loads(raw)

        existing = await self.get_or_create_form_state(session_id, "quote_request")
        for key, val in extracted.items():
            if val is not None and val is not False and val != "":
                existing[key] = val

        await self.db.save_form_state(session_id, "quote_request", existing, "in_progress")

    async def cleanup_expired_memory(self) -> int:
        """Delete session memory older than retention period."""
        retention_days = self.settings.memory_retention_days
        cutoff = (datetime.utcnow() - timedelta(days=retention_days)).isoformat()
        total_deleted = 0
        total_deleted += await self.db.delete_old_messages(cutoff)
        total_deleted += await self.db.delete_old_summaries(cutoff)
        total_deleted += await self.db.delete_old_states(cutoff)
        total_deleted += await self.db.delete_old_form_states(cutoff)
        if total_deleted:
            logger.info(f"Cleaned up {total_deleted} expired memory records")
        return total_deleted


_memory_service: Optional[MemoryService] = None


def get_memory_service() -> MemoryService:
    global _memory_service
    if _memory_service is None:
        _memory_service = MemoryService()
    return _memory_service