# 📖 API Documentation

Complete reference for all RAG Chatbot API endpoints.

**Base URL**: `http://localhost:8000` (development) | `https://your-api.railway.app` (production)

---

## Authentication

Most admin endpoints require authentication via the `X-Admin-Password` header.

```bash
# Include in every admin request
-H "X-Admin-Password: your-admin-password"

# OR using Authorization header
-H "Authorization: Bearer your-admin-password"
```

---

## Health Endpoints

### GET /health

Returns basic health status.

**No authentication required.**

```bash
curl http://localhost:8000/health
```

**Response 200:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "environment": "production"
}
```

---

### GET /health/detailed

Returns detailed health check including all services.

```bash
curl http://localhost:8000/health/detailed
```

**Response 200:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "environment": "production",
  "backend": true,
  "vectordb": true,
  "openai": true,
  "sqlite": true,
  "details": {
    "vector_db_type": "chromadb",
    "openai_model": "gpt-4o-mini",
    "embed_model": "text-embedding-3-small"
  }
}
```

---

## Chat Endpoints

### POST /api/chat

Send a user message and receive an AI-generated response using the RAG pipeline.

**No authentication required.**

```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user-session-abc123",
    "message": "What is your return policy?"
  }'
```

**Request Body:**
```json
{
  "session_id": "string (required, max 128 chars)",
  "message": "string (required, max 2000 chars)"
}
```

**Response 200:**
```json
{
  "response": "You can return most items within 30 days of purchase. Simply visit the returns section of our website or contact our support team. Would you like more details about what items are eligible?",
  "message_id": "7f3a2b4c-1d5e-4f6a-8b9c-0d1e2f3a4b5c",
  "session_id": "user-session-abc123",
  "processing_time_ms": 1245
}
```

**Response 429 (Rate Limited):**
```json
{
  "detail": "Too many requests. Please wait a moment before trying again."
}
```

---

### GET /api/chat/history/{session_id}

Retrieve conversation history for a specific session.

```bash
curl http://localhost:8000/api/chat/history/user-session-abc123
```

**Response 200:**
```json
{
  "session_id": "user-session-abc123",
  "messages": [
    {
      "id": "7f3a2b4c-1d5e-4f6a-8b9c-0d1e2f3a4b5c",
      "session_id": "user-session-abc123",
      "user_message": "What is your return policy?",
      "bot_response": "You can return most items within 30 days...",
      "timestamp": "2024-01-15T14:30:25",
      "rating": 1
    }
  ],
  "total": 1
}
```

---

### POST /api/chat/rating

Submit a thumbs-up/down rating for a bot message.

```bash
curl -X POST http://localhost:8000/api/chat/rating \
  -H "Content-Type: application/json" \
  -d '{
    "message_id": "7f3a2b4c-1d5e-4f6a-8b9c-0d1e2f3a4b5c",
    "rating": 1
  }'
```

**Request Body:**
```json
{
  "message_id": "string (required)",
  "rating": -1 | 0 | 1
}
```

**Response 200:**
```json
{
  "status": "ok",
  "message_id": "7f3a2b4c-...",
  "rating": 1
}
```

---

## Admin — Documents

### POST /api/admin/upload

Upload a document for ingestion into the knowledge base.

```bash
curl -X POST http://localhost:8000/api/admin/upload \
  -H "X-Admin-Password: your-password" \
  -F "file=@/path/to/document.pdf"
```

**Response 201:**
```json
{
  "document_id": "9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d",
  "name": "document.pdf",
  "status": "processing",
  "message": "Document uploaded and queued for processing."
}
```

**Response 415 (Unsupported Type):**
```json
{
  "detail": "Unsupported file type '.exe'. Allowed: .pdf, .txt, .md, .csv, .xlsx, .xls"
}
```

---

### GET /api/admin/documents

List all documents in the knowledge base.

```bash
curl http://localhost:8000/api/admin/documents \
  -H "X-Admin-Password: your-password"
```

**Response 200:**
```json
{
  "documents": [
    {
      "id": "9a8b7c6d-...",
      "name": "product_catalog.pdf",
      "type": "PDF",
      "size": 245760,
      "chunks": 42,
      "status": "indexed",
      "uploaded_at": "2024-01-15T10:00:00",
      "error_msg": null
    }
  ],
  "total": 1
}
```

**Document Status Values:**
| Status | Meaning |
|--------|---------|
| `queued` | Waiting to be processed |
| `processing` | Currently being ingested |
| `indexed` | Ready for search |
| `error` | Processing failed (see `error_msg`) |

---

### DELETE /api/admin/documents/{document_id}

Delete a document and remove its vectors from the knowledge base.

```bash
curl -X DELETE http://localhost:8000/api/admin/documents/9a8b7c6d-... \
  -H "X-Admin-Password: your-password"
```

**Response 204:** *(No content)*

**Response 404:**
```json
{
  "detail": "Document not found."
}
```

---

### POST /api/admin/reindex

Re-process and re-index all documents in the `/documents` folder.

```bash
curl -X POST http://localhost:8000/api/admin/reindex \
  -H "X-Admin-Password: your-password" \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Response 200:**
```json
{
  "status": "started",
  "message": "Re-indexing 5 document(s) in the background.",
  "documents_queued": 5
}
```

---

## Admin — Analytics

### GET /api/admin/analytics

Retrieve aggregated usage analytics.

```bash
# Last 30 days (default)
curl http://localhost:8000/api/admin/analytics \
  -H "X-Admin-Password: your-password"

# Last 7 days
curl "http://localhost:8000/api/admin/analytics?days=7" \
  -H "X-Admin-Password: your-password"
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `days` | integer | 30 | Number of days to look back |

**Response 200:**
```json
{
  "total_queries": 342,
  "avg_response_time_ms": 1847.3,
  "satisfaction_rate": 0.87,
  "error_rate": 0.02,
  "total_documents": 5,
  "total_chunks": 187,
  "daily_stats": [
    {
      "date": "2024-01-15",
      "query_count": 47,
      "avg_response_ms": 1920.5,
      "positive_ratings": 12,
      "negative_ratings": 2
    }
  ],
  "top_questions": [
    {
      "question": "What is your return policy?",
      "count": 28
    },
    {
      "question": "How long does shipping take?",
      "count": 24
    }
  ]
}
```

---

## Admin — Conversations

### GET /api/admin/conversations

List conversation history with pagination.

```bash
# Page 1 (default)
curl http://localhost:8000/api/admin/conversations \
  -H "X-Admin-Password: your-password"

# With search and pagination
curl "http://localhost:8000/api/admin/conversations?page=2&limit=20&search=shipping" \
  -H "X-Admin-Password: your-password"
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number |
| `limit` | integer | 20 | Items per page |
| `search` | string | — | Filter by message content |

**Response 200:**
```json
{
  "conversations": [
    {
      "id": "conv-id-...",
      "session_id": "session-id-...",
      "user_message": "What are your shipping options?",
      "bot_response": "We offer standard (3-5 days), express (1-2 days)...",
      "rating": 1,
      "timestamp": "2024-01-15T14:30:25"
    }
  ],
  "total": 342,
  "page": 1,
  "limit": 20
}
```

---

## Admin — Configuration

### GET /api/admin/config

Get current RAG configuration.

```bash
curl http://localhost:8000/api/admin/config \
  -H "X-Admin-Password: your-password"
```

**Response 200:**
```json
{
  "chunk_size": 800,
  "chunk_overlap": 150,
  "top_k": 5,
  "similarity_threshold": 0.7,
  "model": "gpt-4o-mini",
  "temperature": 0.3,
  "max_tokens": 500,
  "memory_turns": 5,
  "system_prompt": "You are an intelligent customer service assistant...",
  "business_name": "ShopBot AI"
}
```

---

### PUT /api/admin/config

Update RAG configuration. Only include fields you want to change.

```bash
curl -X PUT http://localhost:8000/api/admin/config \
  -H "X-Admin-Password: your-password" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4-turbo",
    "temperature": 0.5,
    "top_k": 7,
    "business_name": "My Amazing Store"
  }'
```

**Response 200:**
```json
{
  "status": "ok",
  "updated_fields": ["model", "temperature", "top_k", "business_name"],
  "message": "Updated 4 configuration field(s)."
}
```

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Human-readable error message"
}
```

| HTTP Status | Meaning |
|-------------|---------|
| 200 | Success |
| 201 | Created |
| 204 | No content (successful delete) |
| 400 | Bad request (invalid input) |
| 401 | Unauthorized (wrong admin password) |
| 404 | Resource not found |
| 413 | File too large |
| 415 | Unsupported media type |
| 422 | Validation error (missing/invalid fields) |
| 429 | Rate limit exceeded |
| 500 | Internal server error |

---

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| `POST /api/chat` | 30 requests/minute per IP |
| Admin endpoints | No rate limit (password protected) |

---

## Interactive Documentation

When running locally, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

*(Disabled in production for security.)*
