    async def watch_folder(self) -> None:
        from app.services.database import get_db

        folder = Path(self.settings.documents_dir)
        folder.mkdir(parents=True, exist_ok=True)
        logger.info(f"Watching folder: {folder}")

        while True:
            try:
                db = get_db()
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
                    if doc_name in indexed_names:
                        continue

                    logger.info(f"Folder watcher: new file detected '{doc_name}'")
                    doc_id = str(uuid.uuid4())
                    await db.create_document(doc_id, doc_name, file_path.stat().st_size, ext.lstrip(".").upper())
                    result = await self.process_file(file_path, doc_id, doc_name)
                    await db.update_document_status(doc_id, result["status"], result.get("chunk_count"))

            except Exception as e:
                logger.error(f"Folder watcher error: {e}")

            await asyncio.sleep(30)
