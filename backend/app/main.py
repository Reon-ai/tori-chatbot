"""
backend/app/main.py
FastAPI application factory.
- Mounts all routers
- Configures CORS
- Registers startup / shutdown lifecycle events
- Exposes /health and /health/detailed endpoints
"""

from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers   import chat, admin, analytics
from app.services.database          import get_db
from app.services.vector_store       import get_vector_store
from app.services.document_processor import get_processor
from app.utils.config  import get_settings
from app.utils.logger  import logger, setup_logger
from app.models.schemas import HealthResponse, DetailedHealthResponse


# ══════════════════════════════════════════════════════════════════
# LIFESPAN (startup + shutdown)
# ══════════════════════════════════════════════════════════════════
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown tasks."""
    settings = get_settings()
    setup_logger("rag_chatbot", level=settings.log_level)

    logger.info("=" * 60)
    logger.info(f"  {settings.app_name} v{settings.version}")
    logger.info(f"  Environment : {settings.environment}")
    logger.info(f"  Vector DB   : {settings.vector_db_type}")
    logger.info("=" * 60)

    # ── Create data directories ──────────────────────────────────
    for d in [settings.documents_dir, settings.vector_db_path, "./data/logs"]:
        Path(d).mkdir(parents=True, exist_ok=True)

    # ── SQLite ───────────────────────────────────────────────────
    db = get_db()
    await db.connect()
    logger.info("✓ SQLite connected")

    # ── Vector store ─────────────────────────────────────────────
    vs = get_vector_store()
    try:
        await vs.initialize()
        logger.info(f"✓ Vector store ({settings.vector_db_type}) ready")
    except Exception as e:
        logger.error(f"✗ Vector store init failed: {e}")
        logger.warning("  → System will run without RAG (responses will be generic)")

    # ── Start folder watcher in background ───────────────────────
    if settings.environment != "test":
        processor = get_processor()
        asyncio.create_task(processor.watch_folder())
        logger.info(f"✓ Document watcher started on '{settings.documents_dir}'")

    # ── Cleanup task ─────────────────────────────────────────────
    async def periodic_cleanup():
        while True:
            await asyncio.sleep(86400)  # Run daily
            await db.cleanup_old_conversations(settings.conversation_retention_days)

    if settings.environment != "test":
        asyncio.create_task(periodic_cleanup())

    logger.info("✓ Server ready — Listening for requests")

    yield  # ← Application runs here

    # ── Shutdown ─────────────────────────────────────────────────
    logger.info("Shutting down…")
    await db.close()
    logger.info("Goodbye!")


# ══════════════════════════════════════════════════════════════════
# APPLICATION FACTORY
# ══════════════════════════════════════════════════════════════════
def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description=(
            "Production-ready RAG Chatbot API for e-commerce. "
            "Retrieval-Augmented Generation with OpenAI + ChromaDB."
        ),
        docs_url="/docs"   if settings.environment != "production" else None,
        redoc_url="/redoc" if settings.environment != "production" else None,
        lifespan=lifespan,
    )

    # ── Middleware ────────────────────────────────────────────────
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=500)

    # ── Routers ───────────────────────────────────────────────────
    app.include_router(chat.router)
    app.include_router(admin.router)
    app.include_router(analytics.router)

    # ── Health endpoints ──────────────────────────────────────────
    @app.get("/health", response_model=HealthResponse, tags=["health"])
    async def health() -> HealthResponse:
        return HealthResponse(
            status="ok",
            version=settings.version,
            environment=settings.environment,
        )

    @app.get("/health/detailed", response_model=DetailedHealthResponse, tags=["health"])
    async def health_detailed() -> DetailedHealthResponse:
        db = get_db()
        vs = get_vector_store()

        sqlite_ok  = await db.health_check()
        vectordb_ok = await vs.health_check() if vs.is_ready else False

        # Check OpenAI quickly (non-blocking)
        openai_ok = False
        if settings.openai_api_key:
            from app.services.rag_service import get_rag_service
            try:
                openai_ok = await asyncio.wait_for(
                    get_rag_service().check_openai(), timeout=3.0
                )
            except Exception:
                openai_ok = False

        all_ok = sqlite_ok and vectordb_ok

        return DetailedHealthResponse(
            status="ok" if all_ok else "degraded",
            version=settings.version,
            environment=settings.environment,
            backend=True,
            vectordb=vectordb_ok,
            openai=openai_ok,
            sqlite=sqlite_ok,
            details={
                "vector_db_type":  settings.vector_db_type,
                "openai_model":    settings.openai_chat_model,
                "embed_model":     settings.openai_embedding_model,
            },
        )

    # ── Root redirect ─────────────────────────────────────────────
    @app.get("/", include_in_schema=False)
    async def root() -> Dict[str, Any]:
        return {
            "name":        settings.app_name,
            "version":     settings.version,
            "status":      "running",
            "docs":        "/docs",
            "health":      "/health",
        }

    return app


# ── Entry point ───────────────────────────────────────────────────
app = create_app()

if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.environment == "development",
        log_level=settings.log_level.lower(),
    )
