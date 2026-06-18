"""
backend/app/services/intent_detector.py
Intent detection service for form triggering.
Uses CONSERVATIVE keyword matching — only triggers on clear action requests.
NEVER triggers when user is asking for information (address, phone, hours).
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from app.utils.logger import logger
from app.utils.config import get_settings


# CONSERVATIVE intent mappings — only clear action requests
INTENT_MAP: Dict[str, Dict[str, Any]] = {
    "get_quote": {
        "form_id": "get_quote",
        "keywords": [
            "quote", "quotation", "get a quote", "need a quote",
            "how much", "what does it cost", "price for", "pricing on",
            "sample", "samples", "tile sample", "free sample",
            "contractor", "trade price", "trade quote", "bulk order",
            "need pricing", "pricing please", "send me a quote",
            "want a quote", "looking for a quote",
        ],
        "weight": 1.0,
    },
    "get_in_touch": {
        "form_id": "get_in_touch",
        "keywords": [
            "contact me", "call me", "call me back", "get in touch",
            "speak to someone", "talk to a person", "speak to sales",
            "human", "representative", "someone call me",
            "visit showroom", "book appointment", "come to store",
            "showroom visit", "want to visit", "book a consultation",
            "pop in", "drop by",
        ],
        "weight": 1.0,
    },
}


class IntentDetector:
    """Detects customer intent from their message."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._compiled_patterns: Dict[str, List[re.Pattern]] = {}
        self._compile_patterns()

    def _compile_patterns(self) -> None:
        for intent_key, intent_data in INTENT_MAP.items():
            patterns = []
            for kw in intent_data["keywords"]:
                if len(kw) <= 4:
                    pattern = re.compile(r'\b' + re.escape(kw) + r'\b', re.IGNORECASE)
                else:
                    pattern = re.compile(re.escape(kw), re.IGNORECASE)
                patterns.append(pattern)
            self._compiled_patterns[intent_key] = patterns

    def detect(self, message: str) -> Optional[Dict[str, Any]]:
        if not message or len(message.strip()) < 2:
            return None

        message_lower = message.lower().strip()
        best_match: Optional[Dict[str, Any]] = None
        best_score = 0.0

        for intent_key, intent_data in INTENT_MAP.items():
            patterns = self._compiled_patterns[intent_key]
            weight = intent_data.get("weight", 1.0)

            for i, pattern in enumerate(patterns):
                if pattern.search(message_lower):
                    keyword = intent_data["keywords"][i]
                    keyword_score = min(1.0, len(keyword) / 15) * weight

                    if message_lower.startswith(keyword.lower()):
                        keyword_score = min(1.0, keyword_score + 0.15)

                    if '?' in message:
                        keyword_score = min(1.0, keyword_score + 0.05)

                    if keyword_score > best_score:
                        best_score = keyword_score
                        best_match = {
                            "intent": intent_key,
                            "form_id": intent_data["form_id"],
                            "confidence": round(best_score, 3),
                            "matched_keyword": keyword,
                        }

        threshold = self.settings.intent_confidence_threshold
        if best_match and best_match["confidence"] >= threshold:
            logger.info(
                f"Intent detected: {best_match['intent']} "
                f"(confidence={best_match['confidence']}, "
                f"keyword='{best_match['matched_keyword']}')"
            )
            return best_match

        return None

    def get_form_message(self, form_id: str) -> str:
        messages = {
            "get_quote": (
                "I'd be happy to help with that! "
                "Please leave your details below and one of our team will get back to you with a quote."
            ),
            "get_in_touch": (
                "No problem — we'll have someone from our team contact you. "
                "Please leave your details below and we'll be in touch shortly."
            ),
        }
        return messages.get(form_id, "Please complete the form below.")


_detector: Optional[IntentDetector] = None


def get_intent_detector() -> IntentDetector:
    global _detector
    if _detector is None:
        _detector = IntentDetector()
    return _detector