# 🛍️ ShopBot AI — Production-Ready RAG Chatbot

A complete, zero-setup **Retrieval-Augmented Generation (RAG)** chatbot system built for e-commerce businesses. Drop in your documents, add your OpenAI API key, and have a fully functional AI assistant running in under 10 minutes.

---

## 📋 Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Quick Start (Docker)](#quick-start-docker)
4. [Quick Start (Local Dev)](#quick-start-local)
5. [Adding Documents](#adding-documents)
6. [Configuration](#configuration)
7. [Accessing the Application](#accessing-the-application)
8. [Admin Panel](#admin-panel)
9. [Architecture](#architecture)
10. [Troubleshooting](#troubleshooting)

---

## ✨ Features

| Feature | Details |
|---------|---------|
| **RAG Pipeline** | OpenAI embeddings + ChromaDB vector search |
| **Smart Chunking** | 800-token chunks with 150-token overlap + MMR re-ranking |
| **Conversation Memory** | Last 5 turns maintained per session |
| **Document Support** | PDF, TXT, MD, CSV, XLSX |
| **Admin Panel** | Upload docs, view analytics, configure settings |
| **Analytics** | Query volume, response times, satisfaction rates |
| **Auto-Ingestion** | Drop files in `/documents` folder — processed automatically |
| **Dark/Light Mode** | Full theme support with system preference detection |
| **Mobile Responsive** | Works on all screen sizes |
| **Zero Source Citations** | Clean, natural responses — no "[Source: doc.pdf]" |
| **Rate Limiting** | 30 requests/minute per IP |
| **Demo Mode** | Works without a backend for UI testing |

---

## 🔧 Prerequisites

| Tool | Minimum Version | Install |
|------|----------------|---------|
| Docker | 24.x | [docker.com](https://www.docker.com/get-started) |
| Docker Compose | 2.x | Included with Docker Desktop |
| OpenAI API Key | — | [platform.openai.com](https://platform.openai.com) |

> **No Docker?** See [Quick Start (Local Dev)](#quick-start-local) for Python-only setup.

---

## 🚀 Quick Start (Docker)

### Step 1 — Clone / Download the project

```bash
git clone https://github.com/your-org/rag-chatbot.git
cd rag-chatbot
```

### Step 2 — Run the setup script

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

The script will:
- Create the `.env` file from `.env.example`
- Create required directories (`data/`, `documents/`, `nginx/certs/`)
- Validate dependencies

### Step 3 — Add your OpenAI API key

Open `.env` in any text editor:

```bash
nano .env
```

Find and update:
```
OPENAI_API_KEY=sk-your-actual-key-here
ADMIN_PASSWORD=your-secure-admin-password
BUSINESS_NAME=Your Business Name
```

Save and close.

### Step 4 — Start the application

```bash
docker-compose up --build
```

Or in the background:
```bash
docker-compose up -d --build
```

Wait about 30 seconds for the backend to initialise, then visit:
- **Chat Interface**: http://localhost
- **Admin Panel**: http://localhost/admin.html
- **API Docs**: http://localhost/docs
- **Health Check**: http://localhost/health

---

## 💻 Quick Start (Local Dev — No Docker)

### Requirements
- Python 3.10+
- pip

### Steps

```bash
# 1. Set up environment
cd rag-chatbot
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 2. Install Python dependencies
cd backend
pip install -r requirements.txt

# 3. Start the backend API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# 4. Open the frontend
# Open index.html in your browser (via a local server)
# e.g., with Python: python -m http.server 3000
```

Open your browser:
- Frontend: http://localhost:3000
- API: http://localhost:8000/docs

Then click the **"Configure"** button in the chat interface and enter `http://localhost:8000` as the backend URL.

---

## 📂 Adding Documents

### Method 1 — Drop & Go (Recommended)

Simply copy your files into the `documents/` folder:

```
documents/
├── product_catalog.pdf
├── shipping_policy.txt
├── return_policy.md
├── faq.csv
└── pricing.xlsx
```

The system automatically detects and processes new files every **10 seconds**.

### Method 2 — Admin Panel Upload

1. Navigate to http://localhost/admin.html
2. Sign in with your admin password
3. Go to the **Documents** tab
4. Drag & drop files or click **Browse Files**

### Method 3 — Manual Script

```bash
# Ingest all files in /documents
python scripts/ingest_documents.py

# Ingest a specific file
python scripts/ingest_documents.py --file /path/to/document.pdf

# Re-index everything
python scripts/ingest_documents.py --reindex
```

### Supported Formats

| Format | Extension | Best For |
|--------|-----------|----------|
| PDF | `.pdf` | Product manuals, policies |
| Text | `.txt` | FAQs, plain content |
| Markdown | `.md`, `.markdown` | Documentation |
| CSV | `.csv` | Product catalogs, pricing |
| Excel | `.xlsx`, `.xls` | Spreadsheets, inventory |

---

## ⚙️ Configuration

All configuration lives in your `.env` file. Key settings:

### Core Settings

```env
# Required
OPENAI_API_KEY=sk-...

# Business
BUSINESS_NAME=Your Store Name

# Security (CHANGE THESE!)
ADMIN_PASSWORD=your-secure-password
```

### RAG Tuning

```env
CHUNK_SIZE=800           # Larger = more context, slower processing
CHUNK_OVERLAP=150        # Higher = less gaps between chunks
TOP_K=5                  # More chunks = more context (costs more tokens)
SIMILARITY_THRESHOLD=0.7 # Higher = stricter relevance filter (0.0–1.0)
OPENAI_CHAT_MODEL=gpt-4o-mini   # or gpt-4-turbo for higher quality
OPENAI_TEMPERATURE=0.3   # Lower = more factual, Higher = more creative
```

### Vector Database Options

```env
# Default (local, no extra setup)
VECTOR_DB_TYPE=chromadb

# Cloud (requires Pinecone account)
VECTOR_DB_TYPE=pinecone
PINECONE_API_KEY=your-key
PINECONE_ENVIRONMENT=us-east-1

# Self-hosted high-performance
VECTOR_DB_TYPE=qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

---

## 🖥️ Accessing the Application

| URL | Description |
|-----|-------------|
| `http://localhost` | Main chat interface |
| `http://localhost/admin.html` | Admin panel (password required) |
| `http://localhost/health` | Backend health check |
| `http://localhost/docs` | Interactive API documentation |
| `http://localhost:8000` | Backend API direct access |

> **Default admin password**: `admin123` — **Change this immediately** in your `.env` file!

---

## 🔐 Admin Panel

The admin panel at `/admin.html` provides:

### Dashboard
- Real-time KPI metrics (total queries, response time, satisfaction rate)
- Weekly query volume chart
- System status (backend, vector DB, OpenAI, SQLite)

### Documents
- View all indexed documents
- Upload new files with drag-and-drop
- Delete documents from the knowledge base
- Trigger manual re-indexing

### Analytics
- Daily query volume over 7/30/90 days
- Query category breakdown (shipping, returns, products, etc.)
- Top 10 most frequently asked questions
- Export to CSV

### Conversations
- Browse all conversation history
- Search by message content
- View full conversation detail
- Export to CSV

### Configuration
- Adjust RAG parameters (chunk size, top-K, temperature)
- Change the LLM model
- Edit the system prompt
- Update business name
- Configure and test backend connection

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Nginx (Port 80)                       │
│     Serves static files + proxies /api/* to FastAPI          │
└──────────────────────────┬──────────────────────────────────┘
                           │
              ┌────────────▼────────────┐
              │   FastAPI Backend       │
              │   (Port 8000)           │
              │                         │
              │  ┌─────────────────┐   │
              │  │   RAG Pipeline  │   │
              │  │  1. Embed query │   │
              │  │  2. Vector search│  │
              │  │  3. Re-rank     │   │
              │  │  4. LLM call    │   │
              │  └────────┬────────┘   │
              └───────────┼────────────┘
                          │
           ┌──────────────┼──────────────┐
           │              │              │
    ┌──────▼──────┐ ┌─────▼─────┐ ┌────▼────┐
    │  ChromaDB   │ │  SQLite   │ │  OpenAI │
    │(Vector DB)  │ │(Conv/Docs)│ │  API    │
    └─────────────┘ └───────────┘ └─────────┘
```

### Key Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Frontend | HTML5/CSS3/JS | Chat UI & Admin Panel |
| API Server | FastAPI (Python) | REST API, RAG orchestration |
| Vector DB | ChromaDB | Semantic document search |
| LLM | OpenAI GPT-4o-mini | Response generation |
| Embeddings | text-embedding-3-small | Document & query vectorisation |
| Database | SQLite | Conversation history & metadata |
| Proxy | Nginx | Static files + API routing |

---

## 🐛 Troubleshooting

### Backend won't start

```bash
# Check logs
docker-compose logs backend

# Common issues:
# 1. Invalid OpenAI key → Check OPENAI_API_KEY in .env
# 2. Port 8000 in use → Change port in docker-compose.yml
# 3. Permissions → Run: chmod -R 755 data/ documents/
```

### Chat shows "Demo Mode" banner

The frontend is running without a backend connection.
1. Click the **Configure** button
2. Enter `http://localhost:8000` (or your deployed URL)
3. Click **Save & Test Connection**

### Documents not indexing

```bash
# Check document processing logs
docker-compose logs backend | grep "Processing\|Error\|indexed"

# Manual ingest
docker-compose exec backend python -c "
import asyncio
from app.services.document_processor import get_processor
asyncio.run(get_processor().watch_folder())
"
```

### OpenAI API errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AuthenticationError` | Invalid API key | Check `OPENAI_API_KEY` |
| `RateLimitError` | Too many requests | Wait or upgrade OpenAI plan |
| `InvalidRequestError` | Token limit exceeded | Reduce `CHUNK_SIZE` or `TOP_K` |
| `InsufficientQuotaError` | Out of credits | Add credits at platform.openai.com |

### Performance issues

- Reduce `TOP_K` from 5 to 3
- Switch to `gpt-3.5-turbo` in `.env`
- Reduce `CHUNK_SIZE` for faster embedding

### Reset everything

```bash
docker-compose down -v    # stops containers AND deletes volumes
rm -rf data/              # clears vector DB and SQLite
docker-compose up --build # fresh start
```

---

## 🔄 Updates

```bash
git pull origin main
docker-compose build --no-cache
docker-compose up -d
```

---

## 📄 License

MIT License — feel free to use and modify for your business.

---

> 💡 **Need help?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed solutions, or [DEPLOYMENT.md](DEPLOYMENT.md) for cloud deployment guides.

---

## 📁 Complete File Structure

```
rag-chatbot/
├── index.html                  ← Main chat interface
├── admin.html                  ← Admin panel
├── sw.js                       ← Service worker (PWA)
│
├── css/
│   ├── style.css               ← Main styles (shared)
│   └── admin.css               ← Admin panel styles
│
├── js/
│   ├── config.js               ← App config & localStorage helpers
│   ├── api.js                  ← HTTP client + demo mode fallback
│   ├── chat.js                 ← Chat UI logic
│   ├── theme.js                ← Dark/light mode + toasts
│   ├── main.js                 ← Chat page entry point
│   └── admin.js                ← Admin panel logic
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── app/
│   │   ├── main.py             ← FastAPI app factory + lifecycle
│   │   ├── models/schemas.py   ← Pydantic request/response models
│   │   ├── routers/
│   │   │   ├── chat.py         ← Chat API endpoints
│   │   │   ├── admin.py        ← Admin API endpoints
│   │   │   └── analytics.py   ← Analytics endpoints
│   │   ├── services/
│   │   │   ├── rag_service.py  ← Core RAG pipeline
│   │   │   ├── vector_store.py ← ChromaDB/Pinecone/Qdrant abstraction
│   │   │   ├── document_processor.py ← File parsing + ingestion
│   │   │   └── database.py    ← SQLite async operations
│   │   └── utils/
│   │       ├── config.py       ← Pydantic Settings
│   │       └── logger.py      ← Rotating file + stdout logging
│   └── tests/
│       └── test_rag_pipeline.py ← 20+ pytest test cases
│
├── documents/                  ← DROP YOUR FILES HERE
│   ├── README.md
│   └── sample_store_knowledge_base.txt  ← Demo knowledge base
│
├── nginx/nginx.conf            ← Reverse proxy config
├── scripts/
│   ├── setup.sh                ← Automated setup script
│   ├── run_dev.sh              ← Development startup
│   └── ingest_documents.py    ← Manual ingestion CLI
│
├── docker-compose.yml          ← Production stack
├── docker-compose.dev.yml      ← Development overrides
├── .env.example                ← Environment template
├── .gitignore
│
├── README.md                   ← This file
├── DEPLOYMENT.md               ← Cloud deployment guides
├── API_DOCUMENTATION.md        ← Full API reference
└── TROUBLESHOOTING.md          ← Common issues & fixes
```
