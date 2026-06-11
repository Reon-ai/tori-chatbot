"""
backend/app/routers/admin.py
Admin API endpoints (password-protected).
POST /api/admin/upload              — upload + ingest document
GET  /api/admin/documents           — list all documents
DELETE /api/admin/documents/{id}    — delete a document
POST /api/admin/reindex             — re-index all documents
GET  /api/admin/conversations       — list conversations
GET  /api/admin/config              — get current RAG config
PUT  /api/admin/config              — update RAG config
"""

from __future__ import annotations

import os
import uuid
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import (
    APIRouter, Depends, File, Header, HTTPException,
    Request, UploadFile, status, BackgroundTasks,
)

from app.models.schemas import (
    DocumentListResponse, DocumentResponse,
    UploadResponse, ReindexResponse,
    ConversationListResponse, ConversationListItem,
    RagConfigResponse, RagConfigUpdate,
)
from app.services.database          import get_db, Database
from app.services.document_processor import get_processor, DocumentProcessor
from app.services.vector_store       import get_vector_store
from app.utils.config  import get_settings
from app.utils.logger  import logger

router = APIRouter(prefix="/api/admin", tags=["admin"])


# ── Admin authentication dependency ───────────────────────────
async def require_admin(
    x_admin_password: Optional[str] = Header(None, alias="X-Admin-Password"),
    authorization:    Optional[str] = Header(None),
) -> None:
    """
    Simple password check via:
    - X-Admin-Password header, OR
    - Authorization: Bearer <password> header
    In production, replace with JWT or OAuth2.
    """
    settings = get_settings()
    provided = None

    if x_admin_password:
        provided = x_admin_password
    elif authorization and authorization.lower().startswith("bearer "):
        provided = authorization[7:]

    if provided != settings.admin_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid admin credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )


# ══════════════════════════════════════════════════════════════════
# DOCUMENTS
# ══════════════════════════════════════════════════════════════════

ALLOWED_EXTENSIONS = {".pdf", ".txt", ".md", ".markdown", ".csv", ".xlsx", ".xls"}


@router.post(
    "/upload",
    response_model=UploadResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
async def upload_document(
    background_tasks: BackgroundTasks,
    file:             UploadFile = File(...),
    db:               Database  = Depends(get_db),
    processor:        DocumentProcessor = Depends(get_processor),
) -> UploadResponse:
    """Upload and asynchronously ingest a document."""
    settings = get_settings()

    # Validate file type
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Unsupported file type '{ext}'. Allowed: {', '.join(ALLOWED_EXTENSIONS)}",
        )

    # Validate file size
    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > settings.max_file_size_mb:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File too large ({size_mb:.1f} MB). Max: {settings.max_file_size_mb} MB",
        )

    # Save to documents folder
    doc_id   = str(uuid.uuid4())
    doc_name = file.filename or f"document_{doc_id}{ext}"
    save_dir = Path(settings.documents_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / f"{doc_id}{ext}"

    with open(save_path, "wb") as f_out:
        f_out.write(content)

    # Record in DB (status = processing)
    await db.create_document(doc_id, doc_name, len(content), ext.lstrip(".").upper())
    await db.update_document_status(doc_id, "processing")

    # Process asynchronously so upload returns fast
    async def ingest():
        result = await processor.process_file(save_path, doc_id, doc_name)
        await db.update_document_status(
            doc_id,
            result["status"],
            result.get("chunk_count"),
            result.get("error"),
        )

    background_tasks.add_task(ingest)
    logger.info(f"Document '{doc_name}' ({size_mb:.2f} MB) queued for ingestion")

    return UploadResponse(
        document_id=doc_id,
        name=doc_name,
        status="processing",
        message="Document uploaded and queued for processing. It will be available in the knowledge base shortly.",
    )


@router.get(
    "/documents",
    response_model=DocumentListResponse,
    dependencies=[Depends(require_admin)],
)
async def list_documents(db: Database = Depends(get_db)) -> DocumentListResponse:
    """List all documents with their processing status."""
    docs = await db.list_documents()
    return DocumentListResponse(
        documents=[
            DocumentResponse(
                id=d["id"],
                name=d["name"],
                type=d["type"],
                size=d["size"],
                chunks=d["chunks"],
                status=d["status"],
                uploaded_at=d["uploaded_at"],
                error_msg=d.get("error_msg"),
            )
            for d in docs
        ],
        total=len(docs),
    )


@router.delete(
    "/documents/{doc_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_admin)],
)
async def delete_document(
    doc_id:    str,
    db:        Database   = Depends(get_db),
    vs:        Any        = Depends(get_vector_store),
) -> None:
    """Delete a document and remove its vectors from the knowledge base."""
    deleted = await db.delete_document(doc_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found.",
        )
    # Remove vectors
    count = await vs.delete_by_document_id(doc_id)
    logger.info(f"Deleted document {doc_id} ({count} vectors removed)")

    # Remove file from disk
    settings = get_settings()
    for ext in ALLOWED_EXTENSIONS:
        p = Path(settings.documents_dir) / f"{doc_id}{ext}"
        if p.exists():
            p.unlink()
            break


@router.post(
    "/reindex",
    response_model=ReindexResponse,
    dependencies=[Depends(require_admin)],
)
async def reindex_all(
    background_tasks: BackgroundTasks,
    db:               Database   = Depends(get_db),
    processor:        DocumentProcessor = Depends(get_processor),
) -> ReindexResponse:
    """Re-process and re-index all documents in the /documents folder."""
    settings   = get_settings()
    folder     = Path(settings.documents_dir)
    files      = [f for f in folder.iterdir() if f.is_file() and f.suffix.lower() in ALLOWED_EXTENSIONS]
    queued     = 0

    async def do_reindex():
        for f in files:
            doc_id = str(uuid.uuid4())
            await db.create_document(doc_id, f.name, f.stat().st_size, f.suffix.lstrip(".").upper())
            result = await processor.process_file(f, doc_id, f.name)
            await db.update_document_status(doc_id, result["status"], result.get("chunk_count"))
            logger.info(f"Re-indexed: {f.name} → {result['status']}")

    background_tasks.add_task(do_reindex)
    queued = len(files)

    return ReindexResponse(
        status="started",
        message=f"Re-indexing {queued} document(s) in the background.",
        documents_queued=queued,
    )


# ══════════════════════════════════════════════════════════════════
# CONVERSATIONS
# ══════════════════════════════════════════════════════════════════

@router.get(
    "/conversations",
    response_model=ConversationListResponse,
    dependencies=[Depends(require_admin)],
)
async def list_conversations(
    page:   int = 1,
    limit:  int = 20,
    search: str = "",
    db:     Database = Depends(get_db),
) -> ConversationListResponse:
    """Paginated list of all conversations."""
    result = await db.list_conversations(page=page, limit=limit, search=search or None)
    from datetime import datetime
    items = [
        ConversationListItem(
            id=c["id"],
            session_id=c["session_id"],
            user_message=c["user_message"],
            bot_response=c["bot_response"],
            rating=c.get("rating"),
            timestamp=datetime.fromisoformat(c["timestamp"]) if isinstance(c["timestamp"], str) else c["timestamp"],
        )
        for c in result["conversations"]
    ]
    return ConversationListResponse(
        conversations=items,
        total=result["total"],
        page=result["page"],
        limit=result["limit"],
    )


# ══════════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════════

@router.get(
    "/config",
    response_model=RagConfigResponse,
    dependencies=[Depends(require_admin)],
)
async def get_config(db: Database = Depends(get_db)) -> RagConfigResponse:
    """Return current RAG configuration."""
    settings = get_settings()

    return RagConfigResponse(
        chunk_size=await db.get_config("chunk_size", settings.chunk_size),
        chunk_overlap=await db.get_config("chunk_overlap", settings.chunk_overlap),
        top_k=await db.get_config("top_k", settings.top_k),
        similarity_threshold=await db.get_config("similarity_threshold", settings.similarity_threshold),
        model=await db.get_config("model", settings.openai_chat_model),
        temperature=await db.get_config("temperature", settings.openai_temperature),
        max_tokens=await db.get_config("max_tokens", settings.openai_max_tokens),
        memory_turns=await db.get_config("memory_turns", settings.memory_turns),
        system_prompt=await db.get_config("system_prompt", settings.system_prompt),
        business_name=await db.get_config("business_name", settings.business_name),
    )


@router.put(
    "/config",
    response_model=Dict[str, Any],
    dependencies=[Depends(require_admin)],
)
async def update_config(
    payload: RagConfigUpdate,
    db:      Database = Depends(get_db),
) -> Dict[str, Any]:
    """Update RAG configuration (stored in SQLite config table)."""
    updated_fields = []
    data = payload.model_dump(exclude_none=True)

    for key, value in data.items():
        await db.set_config(key, value)
        updated_fields.append(key)
        logger.info(f"Config updated: {key} = {value}")

    return {
        "status": "ok",
        "updated_fields": updated_fields,
        "message": f"Updated {len(updated_fields)} configuration field(s).",
    }
