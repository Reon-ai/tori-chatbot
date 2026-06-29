"""
backend/app/routers/chat.py
Chat API endpoints.
POST /api/chat          — send a message & get RAG response
GET  /api/chat/history/{session_id} — retrieve conversation history
POST /api/chat/transcribe — audio to text via OpenAI Whisper
POST /api/chat/image    — image vision analysis via GPT-4o
POST /api/chat/rating   — submit thumbs-up/down feedback
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile, status

from app.models.schemas import (
    ChatRequest, ChatResponse, FormAction,
    ChatHistoryResponse, ChatHistoryItem,
    RatingRequest,
)
from app.services.rag_service import get_rag_service, RAGService
from app.services.database   import get_db, Database
from app.utils.logger  import logger
from app.utils.config  import get_settings

router = APIRouter(prefix="/api/chat", tags=["chat"])


# ── Rate-limit helper (simple in-memory) ──────────────────────
_request_counts: Dict[str, list] = {}

def _check_rate_limit(client_ip: str, limit: int = 30) -> bool:
    import time
    now    = time.time()
    window = 60
    if client_ip not in _request_counts:
        _request_counts[client_ip] = []
    _request_counts[client_ip] = [
        ts for ts in _request_counts[client_ip] if now - ts < window
    ]
    if len(_request_counts[client_ip]) >= limit:
        return False
    _request_counts[client_ip].append(now)
    return True


# ══════════════════════════════════════════════════════════════════
# POST /api/chat
# ══════════════════════════════════════════════════════════════════
@router.post("", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(
    request:     Request,
    payload:     ChatRequest,
    rag_service: RAGService = Depends(get_rag_service),
    db:          Database   = Depends(get_db),
) -> ChatResponse:
    settings   = get_settings()
    client_ip  = request.client.host if request.client else "unknown"

    if not _check_rate_limit(client_ip, limit=settings.rate_limit_per_minute):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please wait a moment before trying again.",
        )

    if not payload.message.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Message cannot be empty.",
        )

    logger.info(
        f"Chat request | session={payload.session_id[:8]} | "
        f"ip={client_ip} | msg='{payload.message[:80]}'"
    )

    result = await rag_service.generate_response(
        session_id=payload.session_id,
        user_message=payload.message,
    )

    message_id = await db.save_conversation(
        session_id=payload.session_id,
        user_message=payload.message,
        bot_response=result["response"],
        retrieved_chunks=result.get("retrieved_chunks", []),
        processing_ms=result.get("processing_ms"),
    )

    raw_fa      = result.get("form_action")
    form_action = FormAction(**raw_fa) if raw_fa else None

    return ChatResponse(
        response=result["response"],
        message_id=message_id,
        session_id=payload.session_id,
        form_action=form_action,
        processing_time_ms=result.get("processing_ms"),
    )


# ══════════════════════════════════════════════════════════════════
# GET /api/chat/history/{session_id}
# ══════════════════════════════════════════════════════════════════
@router.get("/history/{session_id}", response_model=ChatHistoryResponse)
async def get_history(
    session_id: str,
    db:         Database = Depends(get_db),
) -> ChatHistoryResponse:
    messages = await db.get_session_history(session_id, limit=50)
    items = [
        ChatHistoryItem(
            id=m["id"],
            session_id=m["session_id"],
            user_message=m["user_message"],
            bot_response=m["bot_response"],
            timestamp=datetime.fromisoformat(m["timestamp"]),
            rating=m.get("rating"),
        )
        for m in messages
    ]
    return ChatHistoryResponse(
        session_id=session_id,
        messages=items,
        total=len(items),
    )


# ══════════════════════════════════════════════════════════════════
# POST /api/chat/transcribe  — audio → text via OpenAI Whisper
# ══════════════════════════════════════════════════════════════════
@router.post("/transcribe", status_code=status.HTTP_200_OK)
async def transcribe_audio(
    file: UploadFile = File(...),
) -> Dict[str, Any]:
    settings = get_settings()

    if not settings.openai_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OpenAI API key not configured.",
        )

    audio_bytes = await file.read()
    if len(audio_bytes) < 500:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Audio too short — no speech detected.",
        )

    filename = file.filename or "audio.webm"
    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in {"webm", "ogg", "mp4", "wav", "mp3", "m4a"}:
        ext = "webm"

    try:
        import openai
        import io
        client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = f"audio.{ext}"
        response = await client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en",
        )
        transcript = response.text.strip()
        logger.info(f"Whisper transcript: '{transcript[:80]}'")
        return {"transcript": transcript}

    except openai.APIError as e:
        logger.error(f"Whisper API error: {e}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Transcription failed: {str(e)}",
        )
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Transcription error: {str(e)}",
        )


# ══════════════════════════════════════════════════════════════════
# POST /api/chat/image  — image → vision analysis via GPT-4o
# ══════════════════════════════════════════════════════════════════
@router.post("/image", status_code=status.HTTP_200_OK)
async def analyse_image(
    request:    Request,
    file:       UploadFile = File(...),
    session_id: str        = Form(default=""),
    message:    str        = Form(default=""),
    db:         Database   = Depends(get_db),
) -> Dict[str, Any]:
    import base64
    import io
    import openai

    settings  = get_settings()
    client_ip = request.client.host if request.client else "unknown"

    if not _check_rate_limit(client_ip, limit=settings.rate_limit_per_minute):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please wait a moment before trying again.",
        )

    if not settings.openai_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OpenAI API key not configured.",
        )

    filename  = (file.filename or "image.jpg").lower()
    ext       = filename.rsplit(".", 1)[-1] if "." in filename else "jpg"
    mime_map  = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
                 "png": "image/png",  "webp": "image/webp",
                 "gif": "image/gif"}
    if ext not in mime_map:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported image type '.{ext}'. Please upload a JPG, PNG, WEBP or GIF.",
        )
    mime_type = mime_map[ext]

    image_bytes = await file.read()
    if len(image_bytes) < 100:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Image file appears to be empty or corrupt.",
        )
    if len(image_bytes) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Image is too large. Please upload an image under 10 MB.",
        )

    b64      = base64.b64encode(image_bytes).decode("utf-8")
    data_url = f"data:{mime_type};base64,{b64}"

    user_text = (message or "").strip() or (
        "Please look at this image and help me with any relevant tile, "
        "flooring, sanware or installation advice."
    )

    vision_system = (
        f"{settings.system_prompt}\n\n"
        "## VISION MODE\n"
        "The customer has uploaded a photo. Analyse it carefully. "
        "Look for: tile type, size, finish, grout lines, installation quality, "
        "visible damage (cracks, chips, lippage, efflorescence, staining), "
        "waterproofing concerns, sanware style, or any other detail relevant "
        "to Tiletoria's products and services. "
        "Give a concise, practical, professional assessment as Tori. "
        "If you can identify the product or style, do so. "
        "If you see a problem, describe it clearly and advise the next step. "
        "If you cannot determine enough from the image, ask ONE smart follow-up question."
    )

    logger.info(
        f"Image analysis | session={session_id[:8] if session_id else 'anon'} | "
        f"ip={client_ip} | size={len(image_bytes)//1024}KB | ext={ext}"
    )

    try:
        client = openai.AsyncOpenAI(api_key=settings.openai_api_key)
        response = await client.chat.completions.create(
            model="gpt-4o",
            max_tokens=600,
            messages=[
                {"role": "system", "content": vision_system},
                {
                    "role": "user",
                    "content": [
                        {
                            "type":      "image_url",
                            "image_url": {"url": data_url, "detail": "high"},
                        },
                        {"type": "text", "text": user_text},
                    ],
                },
            ],
        )

        tori_response = response.choices[0].message.content.strip()
        logger.info(f"Vision response: '{tori_response[:80]}'")

        effective_session = session_id or "image-anon"
        message_id = await db.save_conversation(
            session_id=effective_session,
            user_message=f"[Photo] {user_text}",
            bot_response=tori_response,
            retrieved_chunks=[],
            processing_ms=None,
        )

        return {
            "response":   tori_response,
            "message_id": message_id,
            "session_id": effective_session,
        }

    except openai.APIError as e:
        logger.error(f"Vision API error: {e}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Image analysis failed: {str(e)}",
        )
    except Exception as e:
        logger.error(f"Vision error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Image analysis error: {str(e)}",
        )


# ══════════════════════════════════════════════════════════════════
# POST /api/chat/rating
# ══════════════════════════════════════════════════════════════════
@router.post("/rating", status_code=status.HTTP_200_OK)
async def submit_rating(
    payload: RatingRequest,
    db:      Database = Depends(get_db),
) -> Dict[str, Any]:
    success = await db.update_rating(payload.message_id, payload.rating)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found.",
        )
    return {"status": "ok", "message_id": payload.message_id, "rating": payload.rating}
