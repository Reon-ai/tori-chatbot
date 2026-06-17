"""
backend/app/models/schemas.py
All Pydantic request/response models used across the application.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, field_validator


# ══════════════════════════════════════════════════════════════════
# CHAT
# ══════════════════════════════════════════════════════════════════

class ChatRequest(BaseModel):
    """Incoming chat message from a user."""
    session_id: str = Field(..., min_length=1, max_length=128, description="Unique session identifier")
    message: str = Field(..., min_length=1, max_length=2000, description="User's message")

    @field_validator("message")
    @classmethod
    def sanitize_message(cls, v: str) -> str:
        return v.strip()


class ChatResponse(BaseModel):
    """Outgoing chat response."""
    response: str
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    processing_time_ms: Optional[int] = None
    type: str = "text"
    form_id: Optional[str] = None


class RatingRequest(BaseModel):
    message_id: str
    rating: int = Field(..., ge=-1, le=1, description="-1 = negative, 0 = neutral, 1 = positive")


class ChatHistoryItem(BaseModel):
    id: str
    session_id: str
    user_message: str
    bot_response: str
    timestamp: datetime
    rating: Optional[int] = None


class ChatHistoryResponse(BaseModel):
    session_id: str
    messages: List[ChatHistoryItem]
    total: int


# ══════════════════════════════════════════════════════════════════
# FORMS
# ══════════════════════════════════════════════════════════════════

class FormField(BaseModel):
    """A single field in a form definition."""
    name: str
    label: str
    type: str
    required: bool = False
    placeholder: Optional[str] = None
    options: Optional[List[str]] = None


class FormDefinition(BaseModel):
    """A complete form definition."""
    id: str
    title: str
    description: str
    fields: List[FormField]


class FormDefinitionSummary(BaseModel):
    """Summary of a form (for listing)."""
    id: str
    title: str
    description: str


class FormSubmitRequest(BaseModel):
    """Request to submit a completed form."""
    form_id: str = Field(..., min_length=1, description="The form ID being submitted")
    data: Dict[str, Any] = Field(..., description="The form field values")
    session_id: Optional[str] = Field(None, description="Chat session ID if available")

    @field_validator("form_id")
    @classmethod
    def validate_form_id(cls, v: str) -> str:
        return v.strip()


class FormSubmitResponse(BaseModel):
    """Response after form submission."""
    success: bool
    submission_id: Optional[str] = None
    message: str = ""
    errors: List[str] = Field(default_factory=list)


class FormSubmissionRecord(BaseModel):
    """A stored form submission record."""
    id: str
    form_id: str
    form_title: str
    data: Dict[str, Any]
    session_id: Optional[str]
    submitted_at: str


# ══════════════════════════════════════════════════════════════════
# DOCUMENTS
# ══════════════════════════════════════════════════════════════════

class DocumentStatus(str):
    QUEUED     = "queued"
    PROCESSING = "processing"
    INDEXED    = "indexed"
    ERROR      = "error"
    ARCHIVED   = "archived"


class DocumentResponse(BaseModel):
    id: str
    name: str
    type: str
    size: int
    chunks: Optional[int] = None
    status: str
    uploaded_at: datetime
    error_msg: Optional[str] = None


class DocumentListResponse(BaseModel):
    documents: List[DocumentResponse]
    total: int


class UploadResponse(BaseModel):
    document_id: str
    name: str
    status: str
    message: str


class ReindexResponse(BaseModel):
    status: str
    message: str
    documents_queued: int


# ══════════════════════════════════════════════════════════════════
# ANALYTICS
# ══════════════════════════════════════════════════════════════════

class DailyStats(BaseModel):
    date: str
    query_count: int
    avg_response_ms: Optional[float] = None
    positive_ratings: int = 0
    negative_ratings: int = 0


class TopQuestion(BaseModel):
    question: str
    count: int


class AnalyticsResponse(BaseModel):
    total_queries: int
    avg_response_time_ms: Optional[float]
    satisfaction_rate: Optional[float]
    error_rate: float
    daily_stats: List[DailyStats]
    top_questions: List[TopQuestion]
    total_documents: int
    total_chunks: int


# ══════════════════════════════════════════════════════════════════
# ADMIN – CONVERSATIONS
# ══════════════════════════════════════════════════════════════════

class ConversationListItem(BaseModel):
    id: str
    session_id: str
    user_message: str
    bot_response: str
    rating: Optional[int]
    timestamp: datetime


class ConversationListResponse(BaseModel):
    conversations: List[ConversationListItem]
    total: int
    page: int
    limit: int


# ══════════════════════════════════════════════════════════════════
# ADMIN – CONFIG
# ══════════════════════════════════════════════════════════════════

class RagConfigUpdate(BaseModel):
    chunk_size: Optional[int] = Field(None, ge=100, le=4000)
    chunk_overlap: Optional[int] = Field(None, ge=0, le=1000)
    top_k: Optional[int] = Field(None, ge=1, le=20)
    similarity_threshold: Optional[float] = Field(None, ge=0.0, le=1.0)
    model: Optional[str] = None
    temperature: Optional[float] = Field(None, ge=0.0, le=2.0)
    max_tokens: Optional[int] = Field(None, ge=100, le=4000)
    memory_turns: Optional[int] = Field(None, ge=1, le=20)
    system_prompt: Optional[str] = None
    business_name: Optional[str] = None


class RagConfigResponse(BaseModel):
    chunk_size: int
    chunk_overlap: int
    top_k: int
    similarity_threshold: float
    model: str
    temperature: float
    max_tokens: int
    memory_turns: int
    system_prompt: str
    business_name: str


# ══════════════════════════════════════════════════════════════════
# HEALTH
# ══════════════════════════════════════════════════════════════════

class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str


class DetailedHealthResponse(BaseModel):
    status: str
    version: str
    environment: str
    backend: bool = True
    vectordb: bool = False
    openai: bool = False
    sqlite: bool = False
    details: Dict[str, Any] = Field(default_factory=dict)