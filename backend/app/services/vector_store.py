"""
backend/app/services/vector_store.py
Abstraction layer over multiple vector database backends.
Supports: ChromaDB (default), Pinecone, Qdrant.
"""

from __future__ import annotations

import hashlib
import time
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass

from app.utils.logger import logger
from app.utils.config import get_settings


@dataclass
class SearchResult:
    chunk_id: str
    text: str
    metadata: Dict[str, Any]
    score: float


class VectorStore:
    """
    Unified vector store client.
    The concrete backend is chosen by settings.vector_db_type.
    """

    def __init__(self) -> None:
        self.settings   = get_settings()
        self._client    = None
        self._collection = None
        self._backend   = self.settings.vector_db_type.lower()
        self._ready     = False

    # ── Initialisation ─────────────────────────────────────────
    async def initialize(self) -> None:
        if self._backend == "chromadb":
            await self._init_chroma()
        elif self._backend == "pinecone":
            await self._init_pinecone()
        elif self._backend == "qdrant":
            await self._init_qdrant()
        else:
            raise ValueError(f"Unknown vector DB type: {self._backend}")
        self._ready = True
        logger.info(f"VectorStore initialised ({self._backend})")

    async def _init_chroma(self) -> None:
        try:
            import chromadb
            from chromadb.config import Settings as ChromaSettings
            import os

            os.makedirs(self.settings.vector_db_path, exist_ok=True)

            self._client = chromadb.PersistentClient(
                path=self.settings.vector_db_path,
                settings=ChromaSettings(anonymized_telemetry=False),
            )
            try:
                self._collection = self._client.get_or_create_collection(
                    name=self.settings.vector_db_collection,
                    metadata={"hnsw:space": "cosine"},
                )
            except Exception as col_err:
                logger.warning(f"get_or_create_collection failed ({col_err}), retrying")
                import time; time.sleep(1)
                self._collection = self._client.get_collection(
                    name=self.settings.vector_db_collection,
                )
            logger.info(
                f"ChromaDB ready. Collection '{self.settings.vector_db_collection}' "
                f"has {self._collection.count()} documents."
            )
        except ImportError:
            raise ImportError("chromadb is not installed. Run: pip install chromadb")

    async def _init_pinecone(self) -> None:
        try:
            from pinecone import Pinecone, ServerlessSpec

            if not self.settings.pinecone_api_key:
                raise ValueError("PINECONE_API_KEY is required when using Pinecone backend.")

            pc = Pinecone(api_key=self.settings.pinecone_api_key)
            index_name = self.settings.pinecone_index_name

            if index_name not in [i.name for i in pc.list_indexes()]:
                pc.create_index(
                    name=index_name,
                    dimension=1536,  # text-embedding-3-small
                    metric="cosine",
                    spec=ServerlessSpec(cloud="aws", region=self.settings.pinecone_environment or "us-east-1"),
                )
                logger.info(f"Created Pinecone index '{index_name}'")

            self._client = pc.Index(index_name)
            logger.info(f"Pinecone connected to index '{index_name}'")
        except ImportError:
            raise ImportError("pinecone is not installed. Run: pip install pinecone-client")

    async def _init_qdrant(self) -> None:
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.models import Distance, VectorParams

            self._client = QdrantClient(
                host=self.settings.qdrant_host,
                port=self.settings.qdrant_port,
            )
            collections = [c.name for c in self._client.get_collections().collections]
            if self.settings.qdrant_collection not in collections:
                self._client.create_collection(
                    collection_name=self.settings.qdrant_collection,
                    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
                )
                logger.info(f"Created Qdrant collection '{self.settings.qdrant_collection}'")
            logger.info(f"Qdrant connected to '{self.settings.qdrant_collection}'")
        except ImportError:
            raise ImportError("qdrant-client is not installed. Run: pip install qdrant-client")

    # ── Add Vectors ────────────────────────────────────────────
    async def add_vectors(
        self,
        chunk_ids: List[str],
        embeddings: List[List[float]],
        texts: List[str],
        metadatas: List[Dict[str, Any]],
    ) -> None:
        if self._backend == "chromadb":
            await self._chroma_upsert(chunk_ids, embeddings, texts, metadatas)
        elif self._backend == "pinecone":
            await self._pinecone_upsert(chunk_ids, embeddings, texts, metadatas)
        elif self._backend == "qdrant":
            await self._qdrant_upsert(chunk_ids, embeddings, texts, metadatas)

    async def _chroma_upsert(self, ids, embeddings, texts, metadatas):
        self._collection.upsert(ids=ids, embeddings=embeddings, documents=texts, metadatas=metadatas)
        logger.debug(f"ChromaDB upserted {len(ids)} vectors")

    async def _pinecone_upsert(self, ids, embeddings, texts, metadatas):
        batch_size = 100
        vectors = [
            {"id": id_, "values": emb, "metadata": {**meta, "text": txt}}
            for id_, emb, txt, meta in zip(ids, embeddings, texts, metadatas)
        ]
        for i in range(0, len(vectors), batch_size):
            self._client.upsert(vectors=vectors[i:i+batch_size])
        logger.debug(f"Pinecone upserted {len(ids)} vectors")

    async def _qdrant_upsert(self, ids, embeddings, texts, metadatas):
        from qdrant_client.models import PointStruct

        points = [
            PointStruct(
                id=abs(hash(id_)) % (2**63),  # Qdrant needs integer IDs
                vector=emb,
                payload={**meta, "text": txt, "chunk_id": id_},
            )
            for id_, emb, txt, meta in zip(ids, embeddings, texts, metadatas)
        ]
        self._client.upsert(collection_name=self.settings.qdrant_collection, points=points)
        logger.debug(f"Qdrant upserted {len(ids)} vectors")

    # ── Search ─────────────────────────────────────────────────
    async def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        filter_metadata: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        if self._backend == "chromadb":
            return await self._chroma_search(query_embedding, top_k, filter_metadata)
        elif self._backend == "pinecone":
            return await self._pinecone_search(query_embedding, top_k, filter_metadata)
        elif self._backend == "qdrant":
            return await self._qdrant_search(query_embedding, top_k, filter_metadata)
        return []

    async def _chroma_search(self, embedding, top_k, filter_metadata) -> List[SearchResult]:
        kwargs = {
            "query_embeddings": [embedding],
            "n_results": min(top_k, max(self._collection.count(), 1)),
            "include": ["documents", "metadatas", "distances"],
        }
        if filter_metadata:
            kwargs["where"] = filter_metadata

        results = self._collection.query(**kwargs)
        output = []
        if not results or not results.get("ids"):
            return output

        for cid, doc, meta, dist in zip(
            results["ids"][0],
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        ):
            # Chroma returns L2 or cosine distance; convert to similarity
            score = 1.0 - dist
            output.append(SearchResult(chunk_id=cid, text=doc, metadata=meta, score=score))

        return sorted(output, key=lambda x: x.score, reverse=True)

    async def _pinecone_search(self, embedding, top_k, filter_metadata) -> List[SearchResult]:
        kwargs = {"vector": embedding, "top_k": top_k, "include_metadata": True}
        if filter_metadata:
            kwargs["filter"] = filter_metadata

        results = self._client.query(**kwargs)
        return [
            SearchResult(
                chunk_id=m["id"],
                text=m["metadata"].get("text", ""),
                metadata=m["metadata"],
                score=m["score"],
            )
            for m in results.get("matches", [])
        ]

    async def _qdrant_search(self, embedding, top_k, filter_metadata) -> List[SearchResult]:
        results = self._client.search(
            collection_name=self.settings.qdrant_collection,
            query_vector=embedding,
            limit=top_k,
        )
        return [
            SearchResult(
                chunk_id=str(r.payload.get("chunk_id", r.id)),
                text=r.payload.get("text", ""),
                metadata=r.payload,
                score=r.score,
            )
            for r in results
        ]

    # ── Delete ─────────────────────────────────────────────────
    async def delete_by_document_id(self, document_id: str) -> int:
        """Remove all chunks belonging to a document. Returns count deleted."""
        if self._backend == "chromadb":
            results = self._collection.get(where={"document_id": document_id})
            ids = results.get("ids", [])
            if ids:
                self._collection.delete(ids=ids)
            logger.info(f"ChromaDB: deleted {len(ids)} chunks for doc {document_id}")
            return len(ids)

        elif self._backend == "pinecone":
            self._client.delete(filter={"document_id": document_id})
            return -1  # Pinecone doesn't return count

        elif self._backend == "qdrant":
            from qdrant_client.models import Filter, FieldCondition, MatchValue
            self._client.delete(
                collection_name=self.settings.qdrant_collection,
                points_selector=Filter(
                    must=[FieldCondition(key="document_id", match=MatchValue(value=document_id))]
                ),
            )
            return -1
        return 0

    # ── Utilities ──────────────────────────────────────────────
    async def count(self) -> int:
        if self._backend == "chromadb" and self._collection:
            return self._collection.count()
        return 0

    async def health_check(self) -> bool:
        try:
            if self._backend == "chromadb":
                _ = self._collection.count()
                return True
            elif self._backend == "pinecone":
                self._client.describe_index_stats()
                return True
            elif self._backend == "qdrant":
                self._client.get_collections()
                return True
        except Exception as e:
            logger.error(f"VectorStore health check failed: {e}")
        return False

    @property
    def is_ready(self) -> bool:
        return self._ready


# Singleton instance
_vector_store: Optional[VectorStore] = None


def get_vector_store() -> VectorStore:
    global _vector_store
    if _vector_store is None:
        _vector_store = VectorStore()
    return _vector_store
