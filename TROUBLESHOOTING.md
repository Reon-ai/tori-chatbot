# 🔧 Troubleshooting Guide

Solutions to the most common issues when running the RAG Chatbot.

---

## Quick Diagnostic

Run this first to identify your issue:

```bash
# Check all container status
docker-compose ps

# View backend logs (last 50 lines)
docker-compose logs --tail=50 backend

# Test health endpoint
curl -v http://localhost:8000/health

# Test the full chat pipeline
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test-123","message":"Hello, can you help me?"}'
```

---

## 🔴 Common Issues

### 1. "Connection refused" / Backend won't start

**Symptoms**: `curl: (7) Failed to connect to localhost port 8000`

**Check 1**: Is the container running?
```bash
docker-compose ps
# If backend shows "Exit 1", check logs:
docker-compose logs backend
```

**Check 2**: Port conflict
```bash
sudo lsof -i :8000
# If something is using port 8000:
# Change in docker-compose.yml: "8001:8000" and restart
```

**Check 3**: Invalid .env file
```bash
# Verify .env exists
ls -la .env

# Verify it has required fields
grep OPENAI_API_KEY .env
```

**Fix**:
```bash
# Rebuild from scratch
docker-compose down
docker-compose up --build
```

---

### 2. OpenAI API Errors

**AuthenticationError: Incorrect API key**
```bash
# Verify your key starts with "sk-"
grep OPENAI_API_KEY .env

# Test the key directly
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer sk-your-key-here"
```

**RateLimitError: You exceeded your current quota**
- This means your OpenAI account has run out of credits
- Add credits at: https://platform.openai.com/account/billing
- Or switch to a cheaper model in `.env`: `OPENAI_CHAT_MODEL=gpt-3.5-turbo`

**InsufficientQuotaError**
- Same as above — add credits or reduce token usage

**Model not found**
```bash
# Valid models (as of 2024):
OPENAI_CHAT_MODEL=gpt-4o-mini      # Recommended (fast, cheap)
OPENAI_CHAT_MODEL=gpt-4-turbo      # Higher quality
OPENAI_CHAT_MODEL=gpt-3.5-turbo    # Budget option
```

---

### 3. Documents Not Indexing

**Symptom**: Files in `/documents` folder but chat doesn't use them

**Check 1**: File format supported?
```
✓ .pdf  .txt  .md  .csv  .xlsx  .xls
✗ .doc  .docx  .pptx  .html  (not supported)
```

**Check 2**: File permissions
```bash
ls -la documents/
# Files must be readable by the Docker container
chmod 644 documents/*.pdf
```

**Check 3**: Check processing logs
```bash
docker-compose logs backend | grep -E "Processing|Error|indexed|chunk"
```

**Check 4**: Try manual ingestion
```bash
# Run inside the backend container
docker-compose exec backend python -c "
import asyncio, sys, uuid
sys.path.insert(0, '.')
from app.services.document_processor import get_processor
from app.services.database import get_db
from app.services.vector_store import get_vector_store

async def run():
    db = get_db()
    vs = get_vector_store()
    await db.connect()
    await vs.initialize()
    p = get_processor()
    result = await p.process_file('/app/documents/your-file.pdf', str(uuid.uuid4()))
    print(result)

asyncio.run(run())
"
```

**Check 5**: Empty PDF
```bash
# Check if PDF has extractable text (some PDFs are image-only)
pdfinfo your-document.pdf
# If Pages: 0 or it can't be read, the PDF may be scanned images
```

**For scanned PDFs** (image-based), you need OCR:
```bash
# Install OCR support
pip install pytesseract pdf2image
sudo apt install tesseract-ocr
```

---

### 4. Responses Are Generic / Not Using Documents

**Symptom**: Bot answers with generic responses instead of document content

**Check 1**: Are documents indexed?
```bash
curl http://localhost:8000/api/admin/documents \
  -H "X-Admin-Password: your-password"
# Look for "status": "indexed"
```

**Check 2**: Similarity threshold too high
```bash
# In .env, lower the threshold:
SIMILARITY_THRESHOLD=0.5   # (default is 0.7)
# Then restart: docker-compose restart backend
```

**Check 3**: Query not matching content
The vector search works on semantic similarity. Try:
- Using keywords from your actual documents
- Making the query more specific

**Check 4**: Check vector DB count
```bash
docker-compose exec backend python -c "
import asyncio
from app.services.vector_store import get_vector_store

async def run():
    vs = get_vector_store()
    await vs.initialize()
    count = await vs.count()
    print(f'Vectors in DB: {count}')

asyncio.run(run())
"
```
If count is 0, re-run ingestion.

---

### 5. Admin Panel Login Fails

**Symptom**: "Incorrect password" even with the right password

**Check**: What is your admin password?
```bash
grep ADMIN_PASSWORD .env
```

**Default password**: `admin123`

**Reset password**:
```bash
nano .env
# Change: ADMIN_PASSWORD=your-new-password
docker-compose restart backend
```

---

### 6. Nginx / Frontend Issues

**502 Bad Gateway**
- Backend is not running or starting up
- Wait 30 seconds after `docker-compose up` and try again
- Check: `docker-compose logs backend`

**"Demo Mode" banner always shows**
1. Click the yellow banner's **"Configure"** button
2. Enter your backend URL (e.g., `http://localhost:8000`)
3. Click **Save & Test Connection**

**Static files 404**
```bash
# Check nginx is running
docker-compose ps nginx
docker-compose logs nginx

# Verify files exist
ls -la index.html admin.html css/ js/
```

---

### 7. Memory / Performance Issues

**Out of memory errors**
```bash
# Reduce workers in backend/Dockerfile
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]

# Or limit memory in docker-compose.yml
services:
  backend:
    mem_limit: 512m
```

**Slow responses (> 5 seconds)**

| Action | Impact |
|--------|--------|
| Switch to `gpt-3.5-turbo` | ~3x faster, cheaper |
| Reduce `TOP_K` from 5 to 3 | Faster retrieval |
| Reduce `CHUNK_SIZE` | Fewer tokens processed |
| Use `text-embedding-3-small` (default) | Already the fastest |

---

### 8. Vector Database Errors

**ChromaDB: "No space left on device"**
```bash
# Check disk usage
df -h
du -sh data/vectordb/

# Clean up old data
docker-compose down
rm -rf data/vectordb/
docker-compose up -d
# Then re-ingest your documents
python scripts/ingest_documents.py
```

**ChromaDB: Corrupt database**
```bash
# Backup and reset
cp -r data/vectordb data/vectordb_backup_$(date +%Y%m%d)
rm -rf data/vectordb/
# Restart and re-index
docker-compose restart backend
python scripts/ingest_documents.py --reindex
```

---

### 9. Docker Issues

**"docker-compose: command not found"**
```bash
# Use the newer syntax
docker compose up   # (no hyphen)

# Or install docker-compose v2
sudo apt install docker-compose-plugin
```

**Permission denied**
```bash
sudo usermod -aG docker $USER
newgrp docker
# Then try again
```

**Port already in use**
```bash
# Find what's using port 80 or 8000
sudo lsof -i :80
sudo lsof -i :8000

# Kill it or change ports in docker-compose.yml
```

---

### 10. SSL / HTTPS Issues

**Certificate errors**
```bash
# Verify certificate files exist
ls -la nginx/certs/

# Check certificate validity
openssl x509 -in nginx/certs/fullchain.pem -noout -dates
```

**Mixed content warnings** (HTTP resources on HTTPS page)
- Make sure your backend URL in the frontend config uses `https://`
- Update `ALLOWED_ORIGINS` to use `https://` in `.env`

---

## 📊 Log Analysis

### Find errors in logs

```bash
# All errors
docker-compose logs backend | grep -i "error\|exception\|failed"

# Slow queries (>3 seconds)
docker-compose logs backend | grep "ms" | awk -F'|' '{if($4>3000) print}'

# Check ingestion status
docker-compose logs backend | grep -E "Processing|indexed|Error"
```

### Enable debug logging

```bash
# In .env:
LOG_LEVEL=DEBUG

docker-compose restart backend

# Now logs show detailed RAG pipeline steps
docker-compose logs -f backend
```

---

## 🆘 Full Reset

If nothing works, start completely fresh:

```bash
# Stop and remove everything (including volumes)
docker-compose down -v

# Remove data
rm -rf data/ documents/*.pdf documents/*.txt

# Rebuild
docker-compose up --build

# Re-add your documents
cp your-files/* documents/

# Re-ingest
docker-compose exec backend python scripts/ingest_documents.py
```

---

## 📞 Getting More Help

1. **Check logs first**: `docker-compose logs backend`
2. **Enable debug**: Set `LOG_LEVEL=DEBUG` in `.env`
3. **Test health**: `curl http://localhost:8000/health/detailed`
4. **Test API directly**: Visit `http://localhost:8000/docs`
5. **Search issues**: Check GitHub Issues in the project repository

---

> 💡 **Pro tip**: 90% of issues are either a missing/invalid `OPENAI_API_KEY` or documents not being processed correctly. Start there!
