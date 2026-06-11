# 🚀 Deployment Guide

Complete step-by-step deployment instructions for multiple platforms.

---

## 📋 Table of Contents

1. [Railway.app (Recommended)](#railwayapp)
2. [Vercel (Frontend) + Railway (Backend)](#vercel--railway)
3. [Docker on VPS / EC2](#docker-on-vps)
4. [Google Cloud Run](#google-cloud-run)
5. [Environment Variables for Production](#production-env-vars)
6. [SSL/HTTPS Setup](#ssl-setup)
7. [Domain Configuration](#domain-configuration)

---

## 🚂 Railway.app

**Best for**: Beginners, full-stack deployment, free tier available.

### Step 1 — Create Railway account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Install the Railway CLI: `npm install -g @railway/cli`

### Step 2 — Create a new project
```bash
railway login
railway init
# Select: Empty project
```

### Step 3 — Deploy the backend

```bash
cd backend
railway up
```

Or via GitHub:
1. Push your code to GitHub
2. In Railway dashboard → **New Project** → **Deploy from GitHub repo**
3. Select your repository
4. Set **Root Directory** to `/backend`
5. Railway auto-detects Python and uses your `requirements.txt`

### Step 4 — Set environment variables

In Railway dashboard → Your service → **Variables** tab:

```
OPENAI_API_KEY=sk-your-key-here
ENVIRONMENT=production
ADMIN_PASSWORD=your-secure-password
VECTOR_DB_TYPE=chromadb
VECTOR_DB_PATH=/app/data/vectordb
SQLITE_PATH=/app/data/chatbot.db
DOCUMENTS_DIR=/app/documents
BUSINESS_NAME=Your Business Name
ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### Step 5 — Add persistent storage

In Railway → Your service → **Volumes** tab:
- Mount path: `/app/data`
- Size: 5 GB (adjust as needed)

### Step 6 — Get your backend URL

After deployment, Railway provides a URL like:
`https://rag-chatbot-production.up.railway.app`

### Step 7 — Configure the frontend

Open `js/config.js` and update, or use the Admin Panel config page to set your backend URL.

> **Cost estimate**: Railway free tier includes 500 hours/month. Production use: ~$5–15/month.

---

## 🔷 Vercel (Frontend) + Railway (Backend)

**Best for**: Maximum performance. CDN-distributed frontend + scalable backend.

### Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com) → **New Project**
2. Import your GitHub repository
3. Set **Root Directory** to `/` (the repo root, which has `index.html`)
4. Set **Framework Preset** to `Other`
5. Build command: *(leave empty)*
6. Output directory: `.` (root)
7. Click **Deploy**

Vercel will give you a URL like `https://your-project.vercel.app`

### Update CORS after Vercel deploy

In Railway environment variables, update:
```
ALLOWED_ORIGINS=https://your-project.vercel.app
```

### Configure backend URL in frontend

After deploying both:
1. Visit your Vercel URL
2. Click the ⚙️ Admin link
3. Go to Configuration
4. Set Backend URL to your Railway URL
5. Save

---

## 🖥️ Docker on VPS

**Best for**: Full control, cost-effective for high traffic.

### Tested on: Ubuntu 22.04 LTS (DigitalOcean, Linode, Hetzner, AWS EC2)

### Step 1 — Provision a server

Minimum specs: 2 CPU, 2 GB RAM, 20 GB SSD
Recommended: 2 CPU, 4 GB RAM, 40 GB SSD

### Step 2 — Initial server setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo apt install docker-compose-plugin -y

# Verify
docker --version
docker compose version
```

### Step 3 — Upload your project

```bash
# From your local machine
scp -r ./rag-chatbot user@your-server-ip:/home/user/

# Or clone from GitHub
ssh user@your-server-ip
git clone https://github.com/your-org/rag-chatbot.git
cd rag-chatbot
```

### Step 4 — Configure environment

```bash
cp .env.example .env
nano .env
# Add your OPENAI_API_KEY and other settings
```

### Step 5 — Launch

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh

docker compose up -d --build
docker compose logs -f   # watch logs
```

### Step 6 — Configure firewall

```bash
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

### Step 7 — Test

```bash
curl http://your-server-ip/health
# Should return: {"status":"ok","version":"1.0.0","environment":"production"}
```

---

## ☁️ Google Cloud Run

**Best for**: Serverless, auto-scaling, pay-per-request.

### Prerequisites
- Google Cloud account with billing enabled
- `gcloud` CLI installed

### Deploy backend

```bash
# Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# Build and push to Google Container Registry
cd backend
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/rag-chatbot-backend

# Deploy to Cloud Run
gcloud run deploy rag-chatbot-backend \
  --image gcr.io/YOUR_PROJECT_ID/rag-chatbot-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --set-env-vars "OPENAI_API_KEY=sk-...,ENVIRONMENT=production,ADMIN_PASSWORD=..."
```

> **Note**: Cloud Run doesn't support persistent volumes by default.
> For persistent ChromaDB, use **Cloud Storage FUSE** or switch to **Pinecone** vector DB.

### Deploy frontend to Firebase Hosting

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

---

## 🔐 Production Environment Variables

**Critical** — change all these before going live:

```env
# MUST CHANGE
OPENAI_API_KEY=sk-your-production-key
ADMIN_PASSWORD=random-secure-password-min-16-chars
ADMIN_SESSION_SECRET=random-32-character-string-here

# MUST UPDATE for your domain
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Recommended settings
ENVIRONMENT=production
LOG_LEVEL=INFO
OPENAI_CHAT_MODEL=gpt-4o-mini
CONVERSATION_RETENTION_DAYS=90
RATE_LIMIT_PER_MINUTE=30

# Vector DB (use Pinecone for multi-instance deployments)
VECTOR_DB_TYPE=chromadb   # or pinecone for cloud deployments
```

### Generate secure secrets

```bash
# Generate ADMIN_PASSWORD
openssl rand -base64 24

# Generate ADMIN_SESSION_SECRET
openssl rand -hex 32
```

---

## 🔒 SSL Setup

### Option A: Let's Encrypt (Free) with Certbot

```bash
# Install Certbot
sudo apt install certbot -y

# Get certificate
sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com

# Certificates are saved to:
# /etc/letsencrypt/live/yourdomain.com/fullchain.pem
# /etc/letsencrypt/live/yourdomain.com/privkey.pem

# Copy to nginx/certs/
mkdir -p nginx/certs
sudo cp /etc/letsencrypt/live/yourdomain.com/fullchain.pem nginx/certs/
sudo cp /etc/letsencrypt/live/yourdomain.com/privkey.pem nginx/certs/
sudo chown $USER:$USER nginx/certs/*
```

Then uncomment the HTTPS server block in `nginx/nginx.conf`.

### Option B: Cloudflare (Easiest)

1. Add your domain to Cloudflare (free)
2. Enable **Flexible SSL** in SSL/TLS settings
3. Cloudflare handles HTTPS → your server can stay on HTTP

### Auto-renewal

```bash
# Add to crontab
echo "0 0 1 * * certbot renew --quiet && docker-compose exec nginx nginx -s reload" | sudo tee -a /etc/crontab
```

---

## 🌐 Domain Configuration

### Point domain to your server

In your domain registrar's DNS settings:
```
A Record:  @    →  your.server.ip.address
A Record:  www  →  your.server.ip.address
```

### Update nginx.conf

Edit `nginx/nginx.conf`, replace `server_name _;` with your domain:
```nginx
server_name yourdomain.com www.yourdomain.com;
```

Restart nginx:
```bash
docker-compose restart nginx
```

---

## 📊 Monitoring (Optional)

### Health check monitoring with UptimeRobot

1. Go to [uptimerobot.com](https://uptimerobot.com) (free tier)
2. Add monitor → HTTP(S)
3. URL: `https://yourdomain.com/health`
4. Alert email when it goes down

### View application logs

```bash
# All logs
docker-compose logs -f

# Backend only
docker-compose logs -f backend

# Last 100 lines
docker-compose logs --tail=100 backend
```

---

## 🔄 Updates & Maintenance

### Update to latest version

```bash
git pull origin main
docker-compose build --no-cache backend
docker-compose up -d backend
```

### Backup your data

```bash
# Backup SQLite database and vector DB
tar -czf backup-$(date +%Y%m%d).tar.gz data/ documents/
```

### Scale for high traffic

```bash
# Run multiple backend instances (requires external vector DB like Pinecone)
docker-compose up -d --scale backend=3
```

---

> 📌 **Railway.app is the recommended deployment platform** for most users — it handles SSL, scaling, and persistence automatically.
