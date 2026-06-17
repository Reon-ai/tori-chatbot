"""
backend/app/services/database.py
SQLite database layer for conversation history and document metadata.
Uses aiosqlite for async access.
"""

from __future__ import annotations

import json
import sqlite3
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

import aiosqlite
from app.utils.logger import logger
from app.utils.config import get_settings


class Database:
    """Async SQLite wrapper."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self.db_path  = self.settings.sqlite_path
        self._conn: Optional[aiosqlite.Connection] = None

    # ── Connection management ──────────────────────────────────
    async def connect(self) -> None:
        Path(self.db_path).parent.mkdir(parents=True, exist_ok=True)
        self._conn = await aiosqlite.connect(self.db_path)
        await self._conn.execute("PRAGMA journal_mode=WAL")
        await self._conn.execute("PRAGMA foreign_keys=ON")
        await self._conn.execute("PRAGMA synchronous=NORMAL")
        await self._create_tables()
        logger.info(f"SQLite database ready at {self.db_path}")

    async def close(self) -> None:
        if self._conn:
            await self._conn.close()
            self._conn = None

    # ── Schema ─────────────────────────────────────────────────
    async def _create_tables(self) -> None:
        sql = """
        CREATE TABLE IF NOT EXISTS conversations (
            id               TEXT PRIMARY KEY,
            session_id       TEXT NOT NULL,
            user_message     TEXT NOT NULL,
            bot_response     TEXT NOT NULL,
            retrieved_chunks TEXT,
            processing_ms    INTEGER,
            rating           INTEGER,
            timestamp        DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX IF NOT EXISTS idx_conv_session   ON conversations(session_id);
        CREATE INDEX IF NOT EXISTS idx_conv_timestamp ON conversations(timestamp);

        CREATE TABLE IF NOT EXISTS documents (
            id          TEXT PRIMARY KEY,
            name        TEXT NOT NULL,
            file_type   TEXT,
            file_size   INTEGER,
            chunk_count INTEGER,
            status      TEXT DEFAULT 'queued',
            error_msg   TEXT,
            uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            indexed_at  DATETIME
        );

        CREATE TABLE IF NOT EXISTS config (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS analytics_events (
            id           TEXT PRIMARY KEY,
            event_type   TEXT NOT NULL,
            session_id   TEXT,
            data         TEXT,
            created_at   DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS form_submissions (
            id          TEXT PRIMARY KEY,
            form_id     TEXT NOT NULL,
            form_title  TEXT NOT NULL,
            data        TEXT NOT NULL,
            session_id  TEXT,
            client_ip   TEXT,
            submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE INDEX IF NOT EXISTS idx_form_sub_form_id ON form_submissions(form_id);
        CREATE INDEX IF NOT EXISTS idx_form_sub_session  ON form_submissions(session_id);
        CREATE INDEX IF NOT EXISTS idx_form_sub_date     ON form_submissions(submitted_at);
        """
        await self._conn.executescript(sql)
        await self._conn.commit()

    # ── Conversations ──────────────────────────────────────────
    async def save_conversation(
        self,
        session_id: str,
        user_message: str,
        bot_response: str,
        retrieved_chunks: Optional[List[str]] = None,
        processing_ms: Optional[int] = None,
    ) -> str:
        conv_id = str(uuid.uuid4())
        await self._conn.execute(
            """
            INSERT INTO conversations (id, session_id, user_message, bot_response,
                                       retrieved_chunks, processing_ms)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                conv_id,
                session_id,
                user_message,
                bot_response,
                json.dumps(retrieved_chunks or []),
                processing_ms,
            ),
        )
        await self._conn.commit()
        return conv_id

    async def get_session_history(
        self, session_id: str, limit: int = 10
    ) -> List[Dict[str, Any]]:
        cursor = await self._conn.execute(
            """
            SELECT id, session_id, user_message, bot_response, timestamp, rating
            FROM conversations
            WHERE session_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
            """,
            (session_id, limit),
        )
        rows = await cursor.fetchall()
        return [
            {
                "id":           row[0],
                "session_id":   row[1],
                "user_message": row[2],
                "bot_response": row[3],
                "timestamp":    row[4],
                "rating":       row[5],
            }
            for row in reversed(rows)
        ]

    async def update_rating(self, message_id: str, rating: int) -> bool:
        cursor = await self._conn.execute(
            "UPDATE conversations SET rating = ? WHERE id = ?",
            (rating, message_id),
        )
        await self._conn.commit()
        return cursor.rowcount > 0

    async def list_conversations(
        self,
        page: int = 1,
        limit: int = 20,
        search: Optional[str] = None,
    ) -> Dict[str, Any]:
        offset = (page - 1) * limit
        where  = ""
        params_count: List[Any] = []
        params_data:  List[Any] = []

        if search:
            where = "WHERE user_message LIKE ? OR bot_response LIKE ?"
            like = f"%{search}%"
            params_count = [like, like]
            params_data  = [like, like, limit, offset]
        else:
            params_data = [limit, offset]

        count_cursor = await self._conn.execute(
            f"SELECT COUNT(*) FROM conversations {where}",
            params_count,
        )
        total = (await count_cursor.fetchone())[0]

        data_cursor = await self._conn.execute(
            f"""
            SELECT id, session_id, user_message, bot_response, rating, timestamp
            FROM conversations {where}
            ORDER BY timestamp DESC
            LIMIT ? OFFSET ?
            """,
            params_data,
        )
        rows = await data_cursor.fetchall()
        items = [
            {
                "id":           row[0],
                "session_id":   row[1],
                "user_message": row[2],
                "bot_response": row[3],
                "rating":       row[4],
                "timestamp":    row[5],
            }
            for row in rows
        ]
        return {"conversations": items, "total": total, "page": page, "limit": limit}

    async def cleanup_old_conversations(self, retention_days: int = 90) -> int:
        cutoff = datetime.utcnow() - timedelta(days=retention_days)
        cursor = await self._conn.execute(
            "DELETE FROM conversations WHERE timestamp < ?",
            (cutoff.isoformat(),),
        )
        await self._conn.commit()
        deleted = cursor.rowcount
        if deleted:
            logger.info(f"Purged {deleted} conversations older than {retention_days} days")
        return deleted

    # ── Documents ──────────────────────────────────────────────
    async def create_document(
        self, doc_id: str, name: str, size: int, file_type: str
    ) -> None:
        await self._conn.execute(
            """
            INSERT OR IGNORE INTO documents (id, name, file_type, file_size, status)
            VALUES (?, ?, ?, ?, 'queued')
            """,
            (doc_id, name, file_type, size),
        )
        await self._conn.commit()

    async def update_document_status(
        self,
        doc_id: str,
        status: str,
        chunk_count: Optional[int] = None,
        error_msg: Optional[str] = None,
    ) -> None:
        indexed_at = datetime.utcnow().isoformat() if status == "indexed" else None
        await self._conn.execute(
            """
            UPDATE documents
            SET status = ?, chunk_count = ?, error_msg = ?, indexed_at = ?
            WHERE id = ?
            """,
            (status, chunk_count, error_msg, indexed_at, doc_id),
        )
        await self._conn.commit()

    async def list_documents(self) -> List[Dict[str, Any]]:
        cursor = await self._conn.execute(
            """
            SELECT id, name, file_type, file_size, chunk_count, status,
                   error_msg, uploaded_at
            FROM documents
            ORDER BY uploaded_at DESC
            """
        )
        rows = await cursor.fetchall()
        return [
            {
                "id":          row[0],
                "name":        row[1],
                "type":        row[2] or "TXT",
                "size":        row[3] or 0,
                "chunks":      row[4],
                "status":      row[5] or "queued",
                "error_msg":   row[6],
                "uploaded_at": row[7],
            }
            for row in rows
        ]

    async def delete_document(self, doc_id: str) -> bool:
        cursor = await self._conn.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
        await self._conn.commit()
        return cursor.rowcount > 0

    async def count_documents(self) -> int:
        cursor = await self._conn.execute("SELECT COUNT(*) FROM documents WHERE status='indexed'")
        return (await cursor.fetchone())[0]

    async def count_chunks(self) -> int:
        cursor = await self._conn.execute("SELECT SUM(chunk_count) FROM documents WHERE status='indexed'")
        val = (await cursor.fetchone())[0]
        return val or 0

    # ── Analytics ──────────────────────────────────────────────
    async def get_analytics(self, days: int = 30) -> Dict[str, Any]:
        cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()

        cursor = await self._conn.execute(
            "SELECT COUNT(*) FROM conversations WHERE timestamp >= ?", (cutoff,)
        )
        total = (await cursor.fetchone())[0]

        cursor = await self._conn.execute(
            "SELECT AVG(processing_ms) FROM conversations WHERE timestamp >= ? AND processing_ms IS NOT NULL",
            (cutoff,),
        )
        avg_ms = (await cursor.fetchone())[0]

        cursor = await self._conn.execute(
            """
            SELECT
                SUM(CASE WHEN rating = 1  THEN 1 ELSE 0 END),
                SUM(CASE WHEN rating = -1 THEN 1 ELSE 0 END)
            FROM conversations
            WHERE timestamp >= ? AND rating IS NOT NULL
            """,
            (cutoff,),
        )
        pos, neg = (await cursor.fetchone())
        pos = pos or 0
        neg = neg or 0

        cursor = await self._conn.execute(
            """
            SELECT date(timestamp) as day, COUNT(*),
                   AVG(processing_ms),
                   SUM(CASE WHEN rating=1 THEN 1 ELSE 0 END),
                   SUM(CASE WHEN rating=-1 THEN 1 ELSE 0 END)
            FROM conversations
            WHERE timestamp >= ?
            GROUP BY day
            ORDER BY day ASC
            """,
            (cutoff,),
        )
        daily = [
            {
                "date":              row[0],
                "query_count":       row[1],
                "avg_response_ms":   row[2],
                "positive_ratings":  row[3] or 0,
                "negative_ratings":  row[4] or 0,
            }
            for row in await cursor.fetchall()
        ]

        cursor = await self._conn.execute(
            """
            SELECT user_message, COUNT(*) as c
            FROM conversations
            WHERE timestamp >= ?
            GROUP BY user_message
            ORDER BY c DESC
            LIMIT 10
            """,
            (cutoff,),
        )
        top_q = [{"question": row[0], "count": row[1]} for row in await cursor.fetchall()]

        rated = pos + neg
        satisfaction = (pos / rated) if rated > 0 else None

        return {
            "total_queries":       total,
            "avg_response_time_ms": avg_ms,
            "satisfaction_rate":   satisfaction,
            "error_rate":          0.0,
            "daily_stats":         daily,
            "top_questions":       top_q,
        }

    # ── Config ─────────────────────────────────────────────────
    async def get_config(self, key: str, default: Any = None) -> Any:
        cursor = await self._conn.execute(
            "SELECT value FROM config WHERE key = ?", (key,)
        )
        row = await cursor.fetchone()
        if row:
            try: return json.loads(row[0])
            except: return row[0]
        return default

    async def set_config(self, key: str, value: Any) -> None:
        await self._conn.execute(
            "INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)",
            (key, json.dumps(value)),
        )
        await self._conn.commit()

    # ── Form Submissions ───────────────────────────────────────
    async def save_form_submission(self, submission: Dict[str, Any]) -> None:
        """Save a form submission to the database."""
        await self._conn.execute(
            """
            INSERT INTO form_submissions (id, form_id, form_title, data, session_id, client_ip, submitted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                submission["id"],
                submission["form_id"],
                submission["form_title"],
                json.dumps(submission["data"]),
                submission.get("session_id"),
                submission.get("client_ip"),
                submission.get("submitted_at", datetime.utcnow().isoformat()),
            ),
        )
        await self._conn.commit()

    async def list_form_submissions(
        self,
        form_id: Optional[str] = None,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        """List form submissions, optionally filtered by form_id."""
        if form_id:
            cursor = await self._conn.execute(
                """
                SELECT id, form_id, form_title, data, session_id, client_ip, submitted_at
                FROM form_submissions
                WHERE form_id = ?
                ORDER BY submitted_at DESC
                LIMIT ?
                """,
                (form_id, limit),
            )
        else:
            cursor = await self._conn.execute(
                """
                SELECT id, form_id, form_title, data, session_id, client_ip, submitted_at
                FROM form_submissions
                ORDER BY submitted_at DESC
                LIMIT ?
                """,
                (limit,),
            )
        rows = await cursor.fetchall()
        return [
            {
                "id": row[0],
                "form_id": row[1],
                "form_title": row[2],
                "data": json.loads(row[3]) if row[3] else {},
                "session_id": row[4],
                "client_ip": row[5],
                "submitted_at": row[6],
            }
            for row in rows
        ]

    # ── Health ─────────────────────────────────────────────────
    async def health_check(self) -> bool:
        try:
            await self._conn.execute("SELECT 1")
            return True
        except Exception:
            return False


# Singleton
_db: Optional[Database] = None


def get_db() -> Database:
    global _db
    if _db is None:
        _db = Database()
    return _db