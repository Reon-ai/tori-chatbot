#!/usr/bin/env python3
"""
scripts/ingest_documents.py
Manual document ingestion script.
Place files in the /documents folder and run:
    python scripts/ingest_documents.py

Or ingest a specific file:
    python scripts/ingest_documents.py --file path/to/document.pdf

Or re-index ALL documents:
    python scripts/ingest_documents.py --reindex
"""

import argparse
import asyncio
import os
import sys
import uuid
from pathlib import Path

# Ensure app package is importable
ROOT = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(ROOT))


async def main():
    parser = argparse.ArgumentParser(description="Ingest documents into the RAG knowledge base")
    parser.add_argument("--file",    type=str, help="Path to a specific file to ingest")
    parser.add_argument("--folder",  type=str, help="Folder to ingest (default: ./documents)")
    parser.add_argument("--reindex", action="store_true", help="Clear and re-index all documents")
    args = parser.parse_args()

    # ── Load settings ─────────────────────────────────────────────
    from dotenv import load_dotenv
    load_dotenv()

    from app.utils.config import get_settings
    from app.services.database          import get_db
    from app.services.vector_store       import get_vector_store
    from app.services.document_processor import get_processor

    settings  = get_settings()
    db        = get_db()
    vs        = get_vector_store()
    processor = get_processor()

    print(f"\n{'='*55}")
    print(f"  RAG Document Ingestion Script")
    print(f"  Vector DB  : {settings.vector_db_type}")
    print(f"  Embed Model: {settings.openai_embedding_model}")
    print(f"{'='*55}\n")

    if not settings.openai_api_key or settings.openai_api_key == "your_key_here":
        print("ERROR: OPENAI_API_KEY is not set in your .env file.")
        sys.exit(1)

    # ── Connect services ─────────────────────────────────────────
    await db.connect()
    await vs.initialize()

    # ── Determine files to process ────────────────────────────────
    allowed_exts = {".pdf", ".txt", ".md", ".markdown", ".csv", ".xlsx", ".xls"}
    files_to_process = []

    if args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"ERROR: File not found: {p}")
            sys.exit(1)
        files_to_process = [p]

    else:
        folder = Path(args.folder or settings.documents_dir)
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
            print(f"Created documents folder: {folder}")
            print("Please add files to this folder and run the script again.")
            sys.exit(0)

        files_to_process = [
            f for f in folder.iterdir()
            if f.is_file() and f.suffix.lower() in allowed_exts
        ]

    if not files_to_process:
        print("No documents found to process.")
        print(f"Add files to: {settings.documents_dir}")
        sys.exit(0)

    print(f"Found {len(files_to_process)} file(s) to process:\n")
    for f in files_to_process:
        print(f"  • {f.name} ({f.stat().st_size / 1024:.1f} KB)")

    print()

    # ── Process each file ────────────────────────────────────────
    success = 0
    errors  = 0

    for file_path in files_to_process:
        doc_id   = str(uuid.uuid4())
        doc_name = file_path.name
        ext      = file_path.suffix.lstrip(".").upper()

        print(f"Processing: {doc_name}")
        await db.create_document(doc_id, doc_name, file_path.stat().st_size, ext)

        try:
            result = await processor.process_file(file_path, doc_id, doc_name)

            if result["status"] == "indexed":
                await db.update_document_status(doc_id, "indexed", result.get("chunk_count"))
                print(f"  ✓ Indexed  | {result.get('chunk_count', '?')} chunks | {result.get('elapsed_s', '?')}s\n")
                success += 1
            else:
                err = result.get("error", "Unknown error")
                await db.update_document_status(doc_id, "error", error_msg=err)
                print(f"  ✗ Error    | {err}\n")
                errors += 1

        except Exception as e:
            await db.update_document_status(doc_id, "error", error_msg=str(e))
            print(f"  ✗ Exception: {e}\n")
            errors += 1

    # ── Summary ──────────────────────────────────────────────────
    print(f"{'='*55}")
    print(f"  Done! ✓ {success} succeeded  ✗ {errors} failed")
    total_docs   = await db.count_documents()
    total_chunks = await db.count_chunks()
    print(f"  Knowledge base: {total_docs} documents, {total_chunks} chunks")
    print(f"{'='*55}\n")

    await db.close()


if __name__ == "__main__":
    asyncio.run(main())
