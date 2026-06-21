"""
backend/app/services/vision_service.py
Image analysis service using OpenAI GPT-4o-mini vision model.
Converts uploaded images into structured text for the RAG pipeline.
"""

from __future__ import annotations

import base64
import json
from typing import Any, Dict, List, Optional

from openai import AsyncOpenAI, APIError, RateLimitError

from app.utils.logger import logger
from app.utils.config import get_settings


_VISION_SYSTEM_PROMPT = """You are a tile and flooring product analysis assistant for Tiletoria, a South African tile retailer.

Analyse the uploaded image carefully. Describe what you can actually see — do not guess or invent details.

Return ONLY a JSON object with this exact structure:

{
  "image_detected": true,
  "image_count": 1,
  "overall_confidence": "high | medium | low",
  "image_type": "tile_damage | product_label | room_scene | installation_issue | quote_request | unknown",
  "visible_items": ["list of visible items"],
  "detected_text": ["any readable text from labels, boxes, stickers"],
  "tile_related_observations": ["specific tile/flooring observations"],
  "possible_customer_intent": "what the customer likely wants help with",
  "recommended_rag_query": "a query to search the tile knowledge base",
  "questions_to_ask_customer": ["follow-up questions if image is unclear"],
  "human_escalation_required": false
}

Rules:
- Use "possible", "appears", "visible" — never state certainty where image is unclear.
- If you see a tile box, barcode, product sticker, shade/batch, or invoice text, extract it.
- If you see damaged tile, describe visible issue only.
- If you see grout haze, lippage, cracking, chipped edges, shade variation — describe carefully.
- If you see a room, identify: bathroom, kitchen, living room, patio, commercial, outdoor, indoor.
- If the image is unclear, ask for: close-up photo, wider room photo, box label, proof of purchase.
- Do not guess exact product names unless label is clearly readable.
- Do not make final warranty decisions.
- Do not diagnose installation failure as fact."""


class VisionService:
    """Analyse uploaded images and convert them to structured text for RAG."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._client: Optional[AsyncOpenAI] = None

    @property
    def client(self) -> AsyncOpenAI:
        if self._client is None:
            if not self.settings.openai_api_key:
                raise ValueError("OPENAI_API_KEY is not configured.")
            self._client = AsyncOpenAI(api_key=self.settings.openai_api_key)
        return self._client

    def validate_images(self, images: List[bytes]) -> Dict[str, Any]:
        """Validate uploaded images before processing."""
        max_images = self.settings.vision_max_images
        max_size_mb = self.settings.vision_max_image_size_mb
        allowed_types = {"image/jpeg", "image/png", "image/webp"}

        if len(images) > max_images:
            return {
                "valid": False,
                "error": f"Too many images. Please upload a maximum of {max_images} images.",
            }

        for i, img_bytes in enumerate(images):
            size_mb = len(img_bytes) / (1024 * 1024)
            if size_mb > max_size_mb:
                return {
                    "valid": False,
                    "error": f"Image {i+1} is too large ({size_mb:.1f}MB). Maximum is {max_size_mb}MB.",
                }

            mime = self._detect_mime(img_bytes)
            if mime not in allowed_types:
                return {
                    "valid": False,
                    "error": f"Unsupported file type for image {i+1}. Please upload JPG, PNG, or WEBP only.",
                }

        return {"valid": True}

    async def analyse_images(self, images: List[bytes], user_message: str = "") -> Dict[str, Any]:
        """Analyse one or more images using the vision model."""
        image_contents = []
        for img_bytes in images:
            mime = self._detect_mime(img_bytes)
            b64 = base64.b64encode(img_bytes).decode("utf-8")
            image_contents.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{mime};base64,{b64}",
                    "detail": "high",
                },
            })

        user_text = user_message.strip() if user_message else "Please analyse this image."

        messages = [
            {"role": "system", "content": _VISION_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_text},
                    *image_contents,
                ],
            },
        ]

        for attempt in range(3):
            try:
                resp = await self.client.chat.completions.create(
                    model=self.settings.vision_model,
                    messages=messages,
                    temperature=0.2,
                    max_tokens=1500,
                    response_format={"type": "json_object"},
                )
                raw = resp.choices[0].message.content.strip()
                analysis = json.loads(raw)

                result = {
                    "image_detected": analysis.get("image_detected", True),
                    "image_count": len(images),
                    "overall_confidence": analysis.get("overall_confidence", "medium"),
                    "image_type": analysis.get("image_type", "unknown"),
                    "visible_items": analysis.get("visible_items", []),
                    "detected_text": analysis.get("detected_text", []),
                    "tile_related_observations": analysis.get("tile_related_observations", []),
                    "possible_customer_intent": analysis.get("possible_customer_intent", ""),
                    "recommended_rag_query": analysis.get("recommended_rag_query", user_message),
                    "questions_to_ask_customer": analysis.get("questions_to_ask_customer", []),
                    "human_escalation_required": analysis.get("human_escalation_required", False),
                }

                logger.info(
                    f"Vision analysis: type={result['image_type']}, "
                    f"confidence={result['overall_confidence']}, "
                    f"intent='{result['possible_customer_intent'][:60]}'"
                )
                return result

            except RateLimitError:
                wait = 2 ** attempt
                logger.warning(f"Vision rate limited, retrying in {wait}s…")
                await __import__("asyncio").sleep(wait)

            except (APIError, json.JSONDecodeError) as e:
                logger.error(f"Vision analysis error (attempt {attempt + 1}): {e}")
                if attempt == 2:
                    return self._fallback_analysis(user_message, len(images))

        return self._fallback_analysis(user_message, len(images))

    @staticmethod
    def build_enhanced_query(user_message: str, image_analysis: Dict[str, Any]) -> str:
        """Combine user message + image analysis into a single RAG query."""
        parts = []

        if user_message.strip():
            parts.append(user_message.strip())

        img_type = image_analysis.get("image_type", "")
        if img_type and img_type != "unknown":
            parts.append(f"[Image type: {img_type.replace('_', ' ')}]")

        observations = image_analysis.get("tile_related_observations", [])
        if observations:
            parts.append("Observations: " + "; ".join(observations))

        detected_text = image_analysis.get("detected_text", [])
        if detected_text:
            parts.append("Detected text: " + "; ".join(detected_text))

        intent = image_analysis.get("possible_customer_intent", "")
        if intent:
            parts.append(f"Customer intent: {intent}")

        recommended = image_analysis.get("recommended_rag_query", "")
        if recommended and len(user_message.strip()) < 20:
            parts.insert(0, recommended)

        return " ".join(parts) if parts else user_message

    @staticmethod
    def _detect_mime(data: bytes) -> str:
        """Detect MIME type from file magic bytes."""
        if data[:2] == b"\xff\xd8":
            return "image/jpeg"
        if data[:4] == b"\x89PNG":
            return "image/png"
        if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
            return "image/webp"
        return "application/octet-stream"

    @staticmethod
    def _fallback_analysis(user_message: str, image_count: int) -> Dict[str, Any]:
        """Return a safe fallback when vision analysis fails."""
        return {
            "image_detected": True,
            "image_count": image_count,
            "overall_confidence": "low",
            "image_type": "unknown",
            "visible_items": [],
            "detected_text": [],
            "tile_related_observations": [],
            "possible_customer_intent": "customer uploaded an image",
            "recommended_rag_query": user_message,
            "questions_to_ask_customer": [
                "Could you describe what the image shows?",
                "If it's a tile product, can you share the product code or name?",
            ],
            "human_escalation_required": False,
        }


_vision_service: Optional[VisionService] = None


def get_vision_service() -> VisionService:
    global _vision_service
    if _vision_service is None:
        _vision_service = VisionService()
    return _vision_service