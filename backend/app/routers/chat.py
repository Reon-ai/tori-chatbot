"""
backend/app/routers/chat.py
Chat API endpoints.
POST /api/chat          — send a message & get RAG response
GET  /api/chat/history/{session_id} — retrieve conversation history
POST /api/chat/transcribe — audio → text via OpenAI Whisper
POST /api/chat/rating   — submit thumbs-up/down feedback
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status

from app.models.schemas import (
    ChatRequest, ChatResponse,
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
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                            detail="Too many requests. Please wait a moment.")
    if not payload.message.strip():
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Message cannot be empty.")
    logger.info(f"Chat request | session={payload.session_id[:8]} | ip={client_ip} | msg='{payload.message[:80]}'")
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
    return ChatResponse(
        response=result["response"],
        message_id=message_id,
        session_id=payload.session_id,
        processing_time_ms=result.get("processing_ms"),
        type=result.get("type", "text"),
        form_id=result.get("form_id"),
        form_prefill=result.get("form_prefill"),
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
    return ChatHistoryResponse(session_id=session_id, messages=items, total=len(items))


# ══════════════════════════════════════════════════════════════════
# POST /api/chat/transcribe  — audio → text via OpenAI Whisper
# ══════════════════════════════════════════════════════════════════
@router.post("/transcribe", status_code=status.HTTP_200_OK)
async def transcribe_audio(
    file: UploadFile = File(...),
) -> Dict[str, Any]:
    """
    Receive audio (webm/ogg) from browser MediaRecorder,
    transcribe via OpenAI Whisper, return text.
    """
    settings = get_settings()
    if not settings.openai_api_key:
        raise HTTPException(status_code=503, detail="OpenAI API key not configured.")

    audio_bytes = await file.read()
    if len(audio_bytes) < 500:
        raise HTTPException(status_code=422, detail="Audio too short — no speech detected.")

    filename = file.filename or "audio.webm"
    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in {"webm", "ogg", "mp4", "wav", "mp3", "m4a"}:
        ext = "webm"

    try:
        import openai, io
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
        raise HTTPException(status_code=502, detail=f"Transcription failed: {str(e)}")
    except Exception as e:
        logger.error(f"Transcription error: {e}")
        raise HTTPException(status_code=500, detail=f"Transcription error: {str(e)}")


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
        raise HTTPException(status_code=404, detail="Message not found.")
    return {"status": "ok", "message_id": payload.message_id, "rating": payload.rating}



  
