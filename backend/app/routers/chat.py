"""
backend/app/routers/chat.py
Chat API endpoints.
POST /api/chat          — send a message & get RAG response
GET  /api/chat/history/{session_id} — retrieve conversation history
POST /api/chat/rating   — submit thumbs-up/down feedback
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status

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
    """
    Allow `limit` requests per minute per IP.
    Returns True if allowed, False if rate-limited.
    """
    import time

    now    = time.time()
    window = 60  # seconds

    if client_ip not in _request_counts:
        _request_counts[client_ip] = []

    # Purge old timestamps
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
    """
    Main chat endpoint.
    - Sanitises input
    - Runs RAG pipeline
    - Saves conversation to SQLite
    - Returns clean response (no source citations)
    """
    settings   = get_settings()
    client_ip  = request.client.host if request.client else "unknown"

    # Rate limiting
    if not _check_rate_limit(client_ip, limit=settings.rate_limit_per_minute):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please wait a moment before trying again.",
        )

    # Input validation
    if not payload.message.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Message cannot be empty.",
        )

    logger.info(
        f"Chat request | session={payload.session_id[:8]} | "
        f"ip={client_ip} | msg='{payload.message[:80]}'"
    )

    # RAG pipeline
    result = await rag_service.generate_response(
        session_id=payload.session_id,
        user_message=payload.message,
    )

    # Persist to DB (sources stored internally, never sent to client)
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
    )


# ══════════════════════════════════════════════════════════════════
# GET /api/chat/history/{session_id}
# ══════════════════════════════════════════════════════════════════
@router.get("/history/{session_id}", response_model=ChatHistoryResponse)
async def get_history(
    session_id: str,
    db:         Database = Depends(get_db),
) -> ChatHistoryResponse:
    """Retrieve conversation history for a session."""
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
# POST /api/chat/rating
# ══════════════════════════════════════════════════════════════════
@router.post("/rating", status_code=status.HTTP_200_OK)
async def submit_rating(
    payload: RatingRequest,
    db:      Database = Depends(get_db),
) -> Dict[str, Any]:
    """Record a thumbs-up/down rating for a bot message."""
    success = await db.update_rating(payload.message_id, payload.rating)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Message not found.",
        )
    return {"status": "ok", "message_id": payload.message_id, "rating": payload.rating}
