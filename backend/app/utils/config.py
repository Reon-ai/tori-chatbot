"""
backend/app/utils/config.py
Centralised configuration using Pydantic BaseSettings.
All values are read from environment variables (or .env file).
"""

from functools import lru_cache
from typing import List, Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ────────────────────────────────────────────
    app_name: str = "RAG Chatbot API"
    environment: str = "development"
    log_level: str = "INFO"
    debug: bool = False
    version: str = "1.0.0"

    # ── CORS ───────────────────────────────────────────────────
    allowed_origins: str = "http://localhost:3000,http://localhost:8080,http://localhost:5500"

    @property
    def origins_list(self) -> List[str]:
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]

    # ── OpenAI ────────────────────────────────────────────────
    openai_api_key: str = ""
    openai_embedding_model: str = "text-embedding-3-small"
    openai_chat_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.3
    openai_max_tokens: int = 500

    # ── Vector DB ─────────────────────────────────────────────
    vector_db_type: str = "chromadb"
    vector_db_path: str = "./data/vectordb"
    vector_db_collection: str = "rag_documents"

    # Pinecone (optional)
    pinecone_api_key: Optional[str] = None
    pinecone_environment: Optional[str] = None
    pinecone_index_name: str = "rag-chatbot"

    # Qdrant (optional)
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_collection: str = "rag_documents"

    # ── SQLite ────────────────────────────────────────────────
    sqlite_path: str = "./data/chatbot.db"

    # ── RAG Parameters ─────────────────────────────────────────
    chunk_size: int = 800
    chunk_overlap: int = 150
    top_k: int = 5
    similarity_threshold: float = 0.7
    memory_turns: int = 5

    # ── Documents ─────────────────────────────────────────────
    documents_dir: str = "./documents"
    max_file_size_mb: int = 50

    # ── Admin ─────────────────────────────────────────────────
    admin_password: str = "admin123"
    admin_session_secret: str = "change-me-in-production-use-random-32-chars"

    # ── Rate limiting ─────────────────────────────────────────
    rate_limit_per_minute: int = 30

    # ── Analytics ─────────────────────────────────────────────
    enable_analytics: bool = True
    conversation_retention_days: int = 90

    # ── Business ──────────────────────────────────────────────
    business_name: str = "ShopBot AI"
    system_prompt: str = """You are an intelligent customer service assistant for {business_name}.

Your role:
- Answer questions about products, orders, shipping, returns, and policies
- Provide accurate information based ONLY on the provided context
- Be helpful, friendly, and concise
- If you don't know something, say so and offer to connect with human support
- Present information naturally without referencing source documents

Context from knowledge base:
{retrieved_context}

Conversation history:
{conversation_history}

Customer question: {user_query}

Guidelines:
- Use natural, conversational language
- Keep responses under 200 words unless detailed explanation needed
- For product recommendations, ask clarifying questions
- For order/shipping issues, direct to appropriate resources
- Always end complex answers asking if user needs more help
- Do NOT mention source documents, citations, or where information came from
- Present all information as if you naturally know it"""

    # ── Email / Notifications ─────────────────────────────────
    notification_email: Optional[str] = None
    smtp_host: Optional[str] = None
    smtp_port: int = 587
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_from: Optional[str] = None

    # ── Form Intent Detection ─────────────────────────────────
    # Minimum confidence threshold (0.0–1.0) to trigger a form
    intent_confidence_threshold: float = 0.45
    # If True, skip RAG and directly return form when intent is detected
    form_short_circuit: bool = True
    # ── Session Memory ────────────────────────────────────────
    # Regenerate summary every N new messages (higher = fewer LLM calls)
    memory_summary_interval: int = 3
    # How many recent messages to send to the AI prompt
    memory_turns: int = 10
    # Days to keep session memory before auto-cleanup
    memory_retention_days: int = 30
    # ── Vision / Image Analysis ───────────────────────────────
    vision_model: str = "gpt-4o-mini"
    vision_max_images: int = 3
    vision_max_image_size_mb: int = 5

    @field_validator("openai_api_key")
    @classmethod
    def validate_openai_key(cls, v: str) -> str:
        if v and not v.startswith("sk-"):
            raise ValueError("OPENAI_API_KEY must start with 'sk-'")
        return v


@lru_cache()
def get_settings() -> Settings:
    """Return cached Settings instance (singleton)."""
    return Settings()