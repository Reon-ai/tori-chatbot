"""
backend/app/services/document_processor.py
Handles ingestion of PDF, TXT, MD, CSV, XLSX files.
Splits into chunks, generates embeddings, stores in vector DB.
"""

from __future__ import annotations

import asyncio
import hashlib
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import aiofiles
from app.utils.logger import logger
from app.utils.config import get_settings
from app.services.vector_store import get_vector_store, VectorStore


class DocumentChunk:
    """A text chunk with metadata."""

    def __init__(
        self,
        chunk_id: str,
        document_id: str,
        document_name: str,
        text: str,
        chunk_index: int,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        self.chunk_id      = chunk_id
        self.document_id   = document_id
        self.document_name = document_name
        self.text          = text
        self.chunk_index   = chunk_index
        self.metadata      = metadata or {}


class DocumentProcessor:
    """
    End-to-end pipeline:
    1. Parse file (PDF / TXT / MD / CSV / XLSX)
    2. Clean and chunk text
    3. Generate embeddings via OpenAI
    4. Store in vector database
    """

    def __init__(self) -> None:
        self.settings     = get_settings()
        self.vector_store = get_vector_store()

    # ── Public entry point ─────────────────────────────────────
    async def process_file(
        self,
        file_path: str | Path,
        document_id: str,
        document_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Process a single file.
        Returns metadata dict with chunk count, status, etc.
        """
        start = time.time()
        path  = Path(file_path)
        name  = document_name or path.name
        ext   = path.suffix.lower()

        logger.info(f"Processing document '{name}' ({ext})")

        try:
            # 1. Extract raw text
            raw_text = await self._extract_text(path, ext)
            if not raw_text.strip():
                return {"status": "error", "error": "No text could be extracted from file."}

            # 2. Chunk
            chunks = self._chunk_text(raw_text, document_id, name)
            logger.info(f"  → {len(chunks)} chunks created")

            # 3. Embed + store in batches
            await self._embed_and_store(chunks)

            elapsed = round(time.time() - start, 2)
            logger.info(f"  ✓ Done in {elapsed}s – {len(chunks)} chunks stored.")

            return {
                "status": "indexed",
                "chunk_count": len(chunks),
                "elapsed_s": elapsed,
            }

        except Exception as e:
            logger.error(f"Error processing '{name}': {e}", exc_info=True)
            return {"status": "error", "error": str(e)}

    # ── Text extraction ─────────────────────────────────────────
    async def _extract_text(self, path: Path, ext: str) -> str:
        if ext == ".pdf":
            return await self._extract_pdf(path)
        elif ext in (".txt", ".md", ".markdown"):
            return await self._extract_text_file(path)
        elif ext == ".csv":
            return await self._extract_csv(path)
        elif ext in (".xlsx", ".xls"):
            return await self._extract_excel(path)
        else:
            # Try reading as plain text
            return await self._extract_text_file(path)

    async def _extract_pdf(self, path: Path) -> str:
        try:
            import pdfplumber
            text_parts = []
            with pdfplumber.open(path) as pdf:
                for i, page in enumerate(pdf.pages):
                    page_text = page.extract_text() or ""
                    if page_text.strip():
                        text_parts.append(f"[Page {i+1}]\n{page_text}")
            return "\n\n".join(text_parts)
        except ImportError:
            pass

        # Fallback: PyPDF2
        try:
            import PyPDF2
            text_parts = []
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for i, page in enumerate(reader.pages):
                    text_parts.append(page.extract_text() or "")
            return "\n\n".join(text_parts)
        except ImportError:
            raise ImportError("Install pdfplumber or PyPDF2: pip install pdfplumber")

    async def _extract_text_file(self, path: Path) -> str:
        async with aiofiles.open(path, "r", encoding="utf-8", errors="ignore") as f:
            return await f.read()

    async def _extract_csv(self, path: Path) -> str:
        try:
            import pandas as pd
            df = pd.read_csv(path)
            lines = []
            for _, row in df.iterrows():
                parts = [f"{col}: {val}" for col, val in row.items() if str(val) != "nan"]
                lines.append(" | ".join(parts))
            return "\n".join(lines)
        except ImportError:
            # Pure stdlib fallback
            import csv
            lines = []
            with open(path, newline="", encoding="utf-8", errors="ignore") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    lines.append(" | ".join(f"{k}: {v}" for k, v in row.items() if v))
            return "\n".join(lines)

    async def _extract_excel(self, path: Path) -> str:
        try:
            import pandas as pd
            all_sheets = pd.read_excel(path, sheet_name=None)
            parts = []
            for sheet_name, df in all_sheets.items():
                parts.append(f"## Sheet: {sheet_name}")
                for _, row in df.iterrows():
                    cells = [f"{col}: {val}" for col, val in row.items() if str(val) != "nan"]
                    parts.append(" | ".join(cells))
            return "\n".join(parts)
        except ImportError:
            raise ImportError("Install pandas + openpyxl: pip install pandas openpyxl")

    # ── Chunking ───────────────────────────────────────────────
    def _chunk_text(
        self,
        text: str,
        document_id: str,
        document_name: str,
    ) -> List[DocumentChunk]:
        """
        Split text into overlapping chunks using a character-based sliding window.
        Uses sentence boundaries where possible to avoid mid-sentence splits.
        """
        chunk_size    = self.settings.chunk_size * 4  # ~4 chars per token
        chunk_overlap = self.settings.chunk_overlap * 4

        # Normalise whitespace
        text = "\n".join(line.rstrip() for line in text.splitlines())
        text = text.strip()

        # Split into sentences/paragraphs first
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        chunks: List[DocumentChunk] = []
        current = ""
        chunk_idx = 0

        for para in paragraphs:
            if not para:
                continue

            if len(current) + len(para) + 2 <= chunk_size:
                current = (current + "\n\n" + para).strip()
            else:
                if current:
                    chunk = self._make_chunk(current, document_id, document_name, chunk_idx)
                    chunks.append(chunk)
                    chunk_idx += 1
                    # Overlap: keep last N chars
                    current = current[-chunk_overlap:] if len(current) > chunk_overlap else current
                    current = (current + "\n\n" + para).strip()
                else:
                    # Para itself is larger than chunk size – force split
                    for i in range(0, len(para), chunk_size - chunk_overlap):
                        part = para[i:i + chunk_size]
                        chunk = self._make_chunk(part, document_id, document_name, chunk_idx)
                        chunks.append(chunk)
                        chunk_idx += 1

        if current.strip():
            chunk = self._make_chunk(current, document_id, document_name, chunk_idx)
            chunks.append(chunk)

        return chunks

    def _make_chunk(
        self, text: str, document_id: str, document_name: str, index: int
    ) -> DocumentChunk:
        chunk_id = hashlib.md5(f"{document_id}-{index}-{text[:64]}".encode()).hexdigest()
        return DocumentChunk(
            chunk_id=chunk_id,
            document_id=document_id,
            document_name=document_name,
            text=text,
            chunk_index=index,
            metadata={
                "document_id":   document_id,
                "document_name": document_name,
                "chunk_index":   index,
            },
        )

    # ── Embedding & storage ─────────────────────────────────────
    async def _embed_and_store(self, chunks: List[DocumentChunk]) -> None:
        """Generate embeddings in batches and store in vector DB."""
        batch_size = 100

        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            texts = [c.text for c in batch]

            embeddings = await self._generate_embeddings(texts)

            chunk_ids  = [c.chunk_id      for c in batch]
            metadatas  = [c.metadata      for c in batch]

            await self.vector_store.add_vectors(
                chunk_ids=chunk_ids,
                embeddings=embeddings,
                texts=texts,
                metadatas=metadatas,
            )
            logger.debug(f"  Stored batch {i//batch_size + 1}: {len(batch)} chunks")

    async def _generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Call OpenAI Embeddings API with retry logic."""
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=self.settings.openai_api_key)

        for attempt in range(3):
            try:
                resp = await client.embeddings.create(
                    model=self.settings.openai_embedding_model,
                    input=texts,
                )
                return [item.embedding for item in resp.data]
            except Exception as e:
                if attempt == 2:
                    raise
                wait = 2 ** attempt
                logger.warning(f"Embedding attempt {attempt+1} failed ({e}), retrying in {wait}s…")
                await asyncio.sleep(wait)

    # ── Folder watcher ─────────────────────────────────────────
    async def watch_folder(self) -> None:
        """
        Monitor the documents folder for new files and process them.
        Only processes files that are NOT already indexed in the database.
        Checks DB on every loop so restarts don't cause re-indexing.
        """
        from app.services.database import get_db

        folder = Path(self.settings.documents_dir)
        folder.mkdir(parents=True, exist_ok=True)
        logger.info(f"Watching folder: {folder}")

        while True:
            try:
                db = get_db()

                # Get all filenames already successfully indexed in DB
                existing_docs = await db.list_documents()
                indexed_names = {
                    d["name"] for d in existing_docs
                    if d.get("status") in ("indexed", "processing")
                }

                for file_path in folder.iterdir():
                    if not file_path.is_file():
                        continue
                    ext = file_path.suffix.lower()
                    if ext not in (".pdf", ".txt", ".md", ".markdown", ".csv", ".xlsx", ".xls"):
                        continue

                    doc_name = file_path.name

                    # Skip if already indexed — this prevents infinite re-indexing
                    if doc_name in indexed_names:
                        continue

                    logger.info(f"Folder watcher: new file detected '{doc_name}'")
                    doc_id = str(uuid.uuid4())
                    await db.create_document(doc_id, doc_name, file_path.stat().st_size, ext.lstrip(".").upper())
                    result = await self.process_file(file_path, doc_id, doc_name)
                    await db.update_document_status(doc_id, result["status"], result.get("chunk_count"))
                    logger.info(f"Folder watcher: '{doc_name}' → {result['status']}")

            except Exception as e:
                logger.error(f"Folder watcher error: {e}")

            await asyncio.sleep(30)


# Singleton
_processor: Optional[DocumentProcessor] = None


def get_processor() -> DocumentProcessor:
    global _processor
    if _processor is None:
        _processor = DocumentProcessor()
    return _processor
