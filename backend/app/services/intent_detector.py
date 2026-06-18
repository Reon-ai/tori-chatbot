"""
backend/app/services/intent_detector.py
Intent detection service for form triggering.

Detects when a customer's message indicates they want to:
- Request a quote
- Get contacted
- Visit a store
- Enquire about a product
- Request samples
- Submit a contractor/trade enquiry

Uses keyword matching for accuracy.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from app.utils.logger import logger
from app.utils.config import get_settings


# Intent keyword mappings
INTENT_MAP: Dict[str, Dict[str, Any]] = {
    "tile_quote": {
        "form_id": "tile_quote",
        "keywords": [
            "quote", "quotation", "price", "pricing", "how much", "cost",
            "estimate", "get a quote", "need a quote", "quote for tiles",
            "tile prices", "what does it cost", "how much are tiles",
            "pricing for", "quote for", "quote on", "quoted",
        ],
        "weight": 1.0,
    },
    "contact_me": {
        "form_id": "contact_me",
        "keywords": [
            "contact me", "call me", "phone me", "get in touch",
            "speak to someone", "talk to a person", "call back",
            "contact us", "reach out", "speak to sales",
            "speak to consultant", "human", "representative",
            "someone call me", "need help from person", "can someone call",
            "chat to someone", "talk to someone", "person to speak to",
        ],
        "weight": 1.0,
    },
    "store_assistance": {
        "form_id": "store_assistance",
        "keywords": [
            "visit store", "come to store", "book appointment", "in-store",
            "showroom", "see products", "look at tiles", "visit branch",
            "booking", "appointment", "can i come in", "store visit",
            "see in person", "visit tiletoria", "book a consultation",
            "consultation", "pop in", "drop by", "come around",
        ],
        "weight": 1.0,
    },
    "product_enquiry": {
        "form_id": "product_enquiry",
        "keywords": [
            "product enquiry", "looking for", "do you have", "stock",
            "availability", "where can i find", "searching for",
            "need a product", "product question", "what products",
            "tile range", "collection", "series", "brand",
            "do you sell", "can i get", "looking for tiles",
            "have you got", "do you stock",
        ],
        "weight": 0.9,
    },
    "sample_request": {
        "form_id": "sample_request",
        "keywords": [
            "sample", "samples", "tile sample", "free sample",
            "get samples", "request sample", "sample tiles",
            "can i get a sample", "send samples", "try before",
            "see the tile", "colour sample", "sample chip",
        ],
        "weight": 1.0,
    },
    "contractor_quote": {
        "form_id": "contractor_quote",
        "keywords": [
            "contractor", "trade quote", "trade price", "bulk order",
            "builder", "developer", "interior designer", "quantity surveyor",
            "architect", "commercial project", "project quote",
            "trade account", "wholesale", "trade pricing", "professional",
            "business account", "bulk pricing", "volume discount",
        ],
        "weight": 1.0,
    },
}


class IntentDetector:
    """
    Detects customer intent from their message.
    Returns the matching form ID if an intent is detected, or None.
    """

    def __init__(self) -> None:
        self.settings = get_settings()
        self._compiled_patterns: Dict[str, List[re.Pattern]] = {}
        self._compile_patterns()

    def _compile_patterns(self) -> None:
        """Pre-compile regex patterns for faster matching."""
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
        """
        Analyse a user message and return form trigger info if intent is detected.
        """
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
        """Return the bot message to show alongside a form."""
        messages = {
            "tile_quote": (
                "I'd be happy to help you with a quote! "
                "Please complete the form below and one of our team members will get back to you with a tailored estimate."
            ),
            "contact_me": (
                "No problem — we'll have someone from our team contact you. "
                "Please fill in your details below and we'll be in touch shortly."
            ),
            "store_assistance": (
                "Great idea — visiting a showroom is the best way to see our ranges. "
                "Please let us know your preferred branch and we'll arrange assistance for you."
            ),
            "product_enquiry": (
                "Let me help you find the right product. "
                "Please provide a few details below and our product specialist will assist you."
            ),
            "sample_request": (
                "We'd be happy to send you samples! "
                "Please complete the request below — you can request up to 5 different tile samples."
            ),
            "contractor_quote": (
                "Thank you for your interest in our trade services. "
                "Please complete the contractor quote form below and our trade team will assist you with competitive pricing."
            ),
        }
        return messages.get(form_id, "Please complete the form below.")


_detector: Optional[IntentDetector] = None


def get_intent_detector() -> IntentDetector:
    global _detector
    if _detector is None:
        _detector = IntentDetector()
    return _detector