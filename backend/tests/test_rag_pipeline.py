"""
backend/tests/test_rag_pipeline.py
Unit tests for core RAG pipeline components.
Run with:  pytest tests/ -v
"""

import asyncio
import json
import sys
import os
import pytest
import pytest_asyncio

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# ══════════════════════════════════════════════════════════════════
# FIXTURES
# ══════════════════════════════════════════════════════════════════

@pytest.fixture(autouse=True)
def set_test_env(monkeypatch, tmp_path):
    """Set test environment variables so no real API calls are made."""
    monkeypatch.setenv("OPENAI_API_KEY",  "sk-test-key-not-real")
    monkeypatch.setenv("ENVIRONMENT",     "test")
    monkeypatch.setenv("VECTOR_DB_PATH",  str(tmp_path / "vectordb"))
    monkeypatch.setenv("SQLITE_PATH",     str(tmp_path / "test.db"))
    monkeypatch.setenv("DOCUMENTS_DIR",   str(tmp_path / "documents"))
    monkeypatch.setenv("ADMIN_PASSWORD",  "testpassword")


# ══════════════════════════════════════════════════════════════════
# CONFIG TESTS
# ══════════════════════════════════════════════════════════════════

class TestConfig:
    def test_settings_loaded(self):
        from app.utils.config import get_settings
        get_settings.cache_clear()
        s = get_settings()
        assert s.app_name == "RAG Chatbot API"
        assert s.environment == "test"

    def test_origins_list(self):
        from app.utils.config import get_settings
        get_settings.cache_clear()
        s = get_settings()
        origins = s.origins_list
        assert isinstance(origins, list)
        assert len(origins) > 0


# ══════════════════════════════════════════════════════════════════
# SCHEMA TESTS
# ══════════════════════════════════════════════════════════════════

class TestSchemas:
    def test_chat_request_valid(self):
        from app.models.schemas import ChatRequest
        req = ChatRequest(session_id="test-session", message="Hello!")
        assert req.session_id == "test-session"
        assert req.message == "Hello!"

    def test_chat_request_strips_whitespace(self):
        from app.models.schemas import ChatRequest
        req = ChatRequest(session_id="s1", message="  Hello world  ")
        assert req.message == "Hello world"

    def test_chat_request_empty_message(self):
        from pydantic import ValidationError
        from app.models.schemas import ChatRequest
        with pytest.raises(ValidationError):
            ChatRequest(session_id="s1", message="")

    def test_rating_valid(self):
        from app.models.schemas import RatingRequest
        r = RatingRequest(message_id="msg-1", rating=1)
        assert r.rating == 1

    def test_rating_out_of_range(self):
        from pydantic import ValidationError
        from app.models.schemas import RatingRequest
        with pytest.raises(ValidationError):
            RatingRequest(message_id="msg-1", rating=5)


# ══════════════════════════════════════════════════════════════════
# RAG SERVICE TESTS (with mocked OpenAI)
# ══════════════════════════════════════════════════════════════════

class TestRAGService:
    def test_preprocess_query(self):
        from app.services.rag_service import RAGService
        service = RAGService()
        # Collapses whitespace
        assert service._preprocess_query("  hello   world  ") == "hello world"
        # Truncates long queries
        long_query = "x" * 2000
        result = service._preprocess_query(long_query)
        assert len(result) <= 1002  # 1000 + ellipsis

    def test_build_context_empty(self):
        from app.services.rag_service import RAGService
        service = RAGService()
        ctx = service._build_context([])
        assert "No specific information" in ctx

    def test_build_context_with_results(self):
        from app.services.rag_service import RAGService
        from app.services.vector_store import SearchResult
        service = RAGService()
        results = [
            SearchResult("id1", "Product A costs $50.", {"doc": "catalog"}, 0.9),
            SearchResult("id2", "Free shipping on $100+.", {"doc": "policy"}, 0.8),
        ]
        ctx = service._build_context(results)
        assert "Product A" in ctx
        assert "Free shipping" in ctx
        assert "[Context 1]" in ctx
        assert "[Context 2]" in ctx

    def test_text_overlap(self):
        from app.services.rag_service import RAGService
        # Identical texts → 1.0
        score = RAGService._text_overlap("hello world", "hello world")
        assert score == 1.0
        # No overlap → 0.0
        score = RAGService._text_overlap("cat dog", "fish bird")
        assert score == 0.0
        # Partial overlap
        score = RAGService._text_overlap("the cat sat", "the dog sat")
        assert 0 < score < 1

    def test_rerank_filters_by_threshold(self):
        from app.services.rag_service import RAGService
        from app.services.vector_store import SearchResult
        from app.utils.config import get_settings
        get_settings.cache_clear()

        service   = RAGService()
        results   = [
            SearchResult("id1", "High relevance text.", {}, 0.95),
            SearchResult("id2", "Low relevance text.",  {}, 0.30),
        ]
        filtered = service._rerank(results, threshold=0.7)
        assert len(filtered) == 1
        assert filtered[0].chunk_id == "id1"

    def test_rerank_graceful_degradation(self):
        """If nothing exceeds threshold, returns best match."""
        from app.services.rag_service import RAGService
        from app.services.vector_store import SearchResult
        service = RAGService()
        results = [SearchResult("id1", "text", {}, 0.2)]
        filtered = service._rerank(results, threshold=0.8)
        assert len(filtered) == 1

    def test_format_history_empty(self):
        from app.services.rag_service import RAGService
        service = RAGService()
        assert "No previous" in service._format_history([])

    def test_format_history(self):
        from app.services.rag_service import RAGService
        service = RAGService()
        history = [
            {"user_message": "Hi",     "bot_response": "Hello!"},
            {"user_message": "Price?", "bot_response": "It's $20."},
        ]
        result = service._format_history(history)
        assert "Customer: Hi" in result
        assert "Assistant: Hello!" in result


# ══════════════════════════════════════════════════════════════════
# DOCUMENT PROCESSOR TESTS
# ══════════════════════════════════════════════════════════════════

class TestDocumentProcessor:
    def test_chunk_text_basic(self, tmp_path):
        from app.services.document_processor import DocumentProcessor
        from app.utils.config import get_settings
        get_settings.cache_clear()

        processor = DocumentProcessor()
        text = "\n\n".join([f"Paragraph {i}. " + "Word " * 100 for i in range(10)])
        chunks = processor._chunk_text(text, "doc-1", "test.txt")
        assert len(chunks) > 1
        for c in chunks:
            assert c.document_id == "doc-1"
            assert c.document_name == "test.txt"
            assert len(c.text) > 0

    def test_chunk_text_small_doc(self, tmp_path):
        from app.services.document_processor import DocumentProcessor
        from app.utils.config import get_settings
        get_settings.cache_clear()

        processor = DocumentProcessor()
        text = "Short document with just one paragraph."
        chunks = processor._chunk_text(text, "doc-2", "small.txt")
        assert len(chunks) == 1
        assert "Short document" in chunks[0].text

    def test_chunk_ids_unique(self, tmp_path):
        from app.services.document_processor import DocumentProcessor
        from app.utils.config import get_settings
        get_settings.cache_clear()

        processor = DocumentProcessor()
        text = "\n\n".join([f"Para {i}: " + "x " * 200 for i in range(5)])
        chunks = processor._chunk_text(text, "doc-3", "multi.txt")
        ids = [c.chunk_id for c in chunks]
        assert len(ids) == len(set(ids)), "Chunk IDs must be unique"

    @pytest.mark.asyncio
    async def test_extract_text_file(self, tmp_path):
        from app.services.document_processor import DocumentProcessor
        get_settings_fn = None
        try:
            from app.utils.config import get_settings
            get_settings.cache_clear()
        except Exception:
            pass

        # Write a test text file
        test_file = tmp_path / "test.txt"
        test_file.write_text("Hello from test file!")

        processor = DocumentProcessor()
        text = await processor._extract_text_file(test_file)
        assert "Hello from test file!" in text

    @pytest.mark.asyncio
    async def test_extract_csv(self, tmp_path):
        from app.services.document_processor import DocumentProcessor
        from app.utils.config import get_settings
        get_settings.cache_clear()

        test_csv = tmp_path / "products.csv"
        test_csv.write_text("name,price,stock\nWidget A,9.99,100\nWidget B,19.99,50\n")

        processor = DocumentProcessor()
        text = await processor._extract_csv(test_csv)
        assert "Widget A" in text
        assert "9.99" in text


# ══════════════════════════════════════════════════════════════════
# DATABASE TESTS
# ══════════════════════════════════════════════════════════════════

class TestDatabase:
    @pytest.mark.asyncio
    async def test_connect_and_tables(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SQLITE_PATH", str(tmp_path / "test.db"))
        from app.utils.config import get_settings
        get_settings.cache_clear()

        from app.services.database import Database
        db = Database()
        await db.connect()

        ok = await db.health_check()
        assert ok is True
        await db.close()

    @pytest.mark.asyncio
    async def test_save_and_retrieve_conversation(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SQLITE_PATH", str(tmp_path / "conv.db"))
        from app.utils.config import get_settings
        get_settings.cache_clear()

        from app.services.database import Database
        db = Database()
        await db.connect()

        msg_id = await db.save_conversation(
            session_id="sess-1",
            user_message="What is your return policy?",
            bot_response="You can return items within 30 days.",
            retrieved_chunks=["chunk-1"],
            processing_ms=450,
        )
        assert msg_id is not None

        history = await db.get_session_history("sess-1", limit=10)
        assert len(history) == 1
        assert history[0]["user_message"] == "What is your return policy?"

        await db.close()

    @pytest.mark.asyncio
    async def test_document_lifecycle(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SQLITE_PATH", str(tmp_path / "docs.db"))
        from app.utils.config import get_settings
        get_settings.cache_clear()

        from app.services.database import Database
        db = Database()
        await db.connect()

        await db.create_document("doc-1", "catalog.pdf", 10240, "PDF")
        docs = await db.list_documents()
        assert len(docs) == 1
        assert docs[0]["name"] == "catalog.pdf"
        assert docs[0]["status"] == "queued"

        await db.update_document_status("doc-1", "indexed", chunk_count=42)
        docs = await db.list_documents()
        assert docs[0]["status"] == "indexed"
        assert docs[0]["chunks"] == 42

        deleted = await db.delete_document("doc-1")
        assert deleted is True
        docs = await db.list_documents()
        assert len(docs) == 0

        await db.close()

    @pytest.mark.asyncio
    async def test_rating_update(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SQLITE_PATH", str(tmp_path / "rating.db"))
        from app.utils.config import get_settings
        get_settings.cache_clear()

        from app.services.database import Database
        db = Database()
        await db.connect()

        msg_id = await db.save_conversation("s1", "q?", "a!", [], 200)
        ok = await db.update_rating(msg_id, 1)
        assert ok is True

        history = await db.get_session_history("s1")
        assert history[0]["rating"] == 1

        # Non-existent message
        ok2 = await db.update_rating("non-existent", 1)
        assert ok2 is False

        await db.close()

    @pytest.mark.asyncio
    async def test_analytics(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SQLITE_PATH", str(tmp_path / "an.db"))
        from app.utils.config import get_settings
        get_settings.cache_clear()

        from app.services.database import Database
        db = Database()
        await db.connect()

        # Insert sample data
        for i in range(5):
            await db.save_conversation(f"s{i}", f"Q{i}", f"A{i}", [], 300)

        data = await db.get_analytics(days=30)
        assert data["total_queries"] == 5

        await db.close()


# ══════════════════════════════════════════════════════════════════
# API ENDPOINT TESTS (using FastAPI TestClient)
# ══════════════════════════════════════════════════════════════════

class TestAPIEndpoints:
    @pytest.fixture
    def test_client(self, tmp_path, monkeypatch):
        """Create a test FastAPI client with isolated database."""
        monkeypatch.setenv("SQLITE_PATH",    str(tmp_path / "api_test.db"))
        monkeypatch.setenv("VECTOR_DB_PATH", str(tmp_path / "vectordb"))
        monkeypatch.setenv("DOCUMENTS_DIR",  str(tmp_path / "documents"))
        monkeypatch.setenv("ENVIRONMENT",    "test")

        from app.utils.config import get_settings
        get_settings.cache_clear()

        # Reset singletons
        import app.services.database as db_mod
        import app.services.vector_store as vs_mod
        import app.services.rag_service  as rag_mod
        db_mod._db             = None
        vs_mod._vector_store   = None
        rag_mod._rag_service   = None

        from fastapi.testclient import TestClient
        from app.main import create_app

        application = create_app()
        client      = TestClient(application, raise_server_exceptions=False)
        return client

    def test_health_endpoint(self, test_client):
        resp = test_client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "version" in data

    def test_root_endpoint(self, test_client):
        resp = test_client.get("/")
        assert resp.status_code == 200
        data = resp.json()
        assert "name" in data

    def test_admin_requires_auth(self, test_client):
        resp = test_client.get("/api/admin/documents")
        assert resp.status_code == 401

    def test_admin_with_correct_password(self, test_client):
        resp = test_client.get(
            "/api/admin/documents",
            headers={"X-Admin-Password": "testpassword"},
        )
        assert resp.status_code == 200

    def test_admin_with_wrong_password(self, test_client):
        resp = test_client.get(
            "/api/admin/documents",
            headers={"X-Admin-Password": "wrongpassword"},
        )
        assert resp.status_code == 401

    def test_upload_invalid_file_type(self, test_client):
        import io
        resp = test_client.post(
            "/api/admin/upload",
            headers={"X-Admin-Password": "testpassword"},
            files={"file": ("test.exe", io.BytesIO(b"binary"), "application/octet-stream")},
        )
        assert resp.status_code == 415

    def test_chat_history_empty(self, test_client):
        resp = test_client.get("/api/chat/history/non-existent-session")
        assert resp.status_code == 200
        data = resp.json()
        assert data["messages"] == []
        assert data["total"] == 0
