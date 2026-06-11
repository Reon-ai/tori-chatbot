#!/usr/bin/env bash
# ================================================================
# scripts/setup.sh
# Automated setup script for the RAG Chatbot system.
# Run:  chmod +x scripts/setup.sh && ./scripts/setup.sh
# ================================================================

set -euo pipefail

# ── Colours ───────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'   # No colour

log_info()    { echo -e "${BLUE}ℹ  $*${NC}"; }
log_success() { echo -e "${GREEN}✓  $*${NC}"; }
log_warn()    { echo -e "${YELLOW}⚠  $*${NC}"; }
log_error()   { echo -e "${RED}✗  $*${NC}"; }
log_step()    { echo -e "\n${BOLD}${BLUE}── $* ──────────────────────${NC}"; }

# ── Header ────────────────────────────────────────────────────────
clear
echo -e "${BOLD}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║        🛍️  RAG Chatbot — Automated Setup                 ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# ── Check current directory ───────────────────────────────────────
if [ ! -f "docker-compose.yml" ]; then
    log_error "Please run this script from the project root directory."
    log_error "Example: cd rag-chatbot && ./scripts/setup.sh"
    exit 1
fi

# ══════════════════════════════════════════════════════════════════
# STEP 1: Check Prerequisites
# ══════════════════════════════════════════════════════════════════
log_step "Checking prerequisites"

# Docker
if command -v docker &>/dev/null; then
    DOCKER_VERSION=$(docker --version | grep -oP '[\d.]+' | head -1)
    log_success "Docker ${DOCKER_VERSION} found"
else
    log_error "Docker is not installed."
    echo "  Install from: https://www.docker.com/get-started"
    exit 1
fi

# Docker Compose
if docker compose version &>/dev/null 2>&1; then
    COMPOSE_VERSION=$(docker compose version --short 2>/dev/null || echo "v2.x")
    log_success "Docker Compose ${COMPOSE_VERSION} found"
elif command -v docker-compose &>/dev/null; then
    COMPOSE_VERSION=$(docker-compose --version | grep -oP '[\d.]+' | head -1)
    log_success "Docker Compose ${COMPOSE_VERSION} found (legacy)"
    # Create alias for rest of script
    shopt -s expand_aliases 2>/dev/null || true
    alias docker-compose-cmd='docker-compose'
else
    log_error "Docker Compose is not installed."
    echo "  It's included with Docker Desktop, or install: sudo apt install docker-compose-plugin"
    exit 1
fi

# curl (for health checks)
if command -v curl &>/dev/null; then
    log_success "curl found"
else
    log_warn "curl not found — health check at end will be skipped"
fi

# ══════════════════════════════════════════════════════════════════
# STEP 2: Create directory structure
# ══════════════════════════════════════════════════════════════════
log_step "Creating directory structure"

DIRS=("data" "data/vectordb" "data/logs" "documents" "nginx/certs")
for dir in "${DIRS[@]}"; do
    mkdir -p "$dir"
    log_success "Created: $dir/"
done

# Create placeholder files to preserve dirs in git
touch data/.gitkeep
touch documents/.gitkeep

# ══════════════════════════════════════════════════════════════════
# STEP 3: Create .env file
# ══════════════════════════════════════════════════════════════════
log_step "Setting up environment configuration"

if [ -f ".env" ]; then
    log_warn ".env file already exists — keeping existing configuration"
    log_info "To reset: rm .env && ./scripts/setup.sh"
else
    cp .env.example .env
    log_success "Created .env from .env.example"
fi

# ══════════════════════════════════════════════════════════════════
# STEP 4: Prompt for OpenAI API key
# ══════════════════════════════════════════════════════════════════
log_step "OpenAI API Key"

# Check if key already set
CURRENT_KEY=$(grep "^OPENAI_API_KEY=" .env | cut -d'=' -f2)
if [[ "$CURRENT_KEY" == "sk-your-openai-api-key-here" ]] || [[ -z "$CURRENT_KEY" ]]; then
    echo ""
    echo "  You need an OpenAI API key to use the RAG pipeline."
    echo "  Get one at: https://platform.openai.com/api-keys"
    echo ""
    read -r -p "  Enter your OpenAI API key (or press Enter to skip): " OPENAI_KEY

    if [[ -n "$OPENAI_KEY" ]]; then
        if [[ "$OPENAI_KEY" == sk-* ]]; then
            # Use sed to replace the key in .env
            if [[ "$OSTYPE" == "darwin"* ]]; then
                sed -i '' "s|^OPENAI_API_KEY=.*|OPENAI_API_KEY=${OPENAI_KEY}|" .env
            else
                sed -i "s|^OPENAI_API_KEY=.*|OPENAI_API_KEY=${OPENAI_KEY}|" .env
            fi
            log_success "OpenAI API key saved"
        else
            log_warn "Key doesn't start with 'sk-' — please verify it's correct"
        fi
    else
        log_warn "No key entered — you'll need to add it manually to .env before the chatbot works"
    fi
else
    log_success "OpenAI API key already configured"
fi

# ══════════════════════════════════════════════════════════════════
# STEP 5: Prompt for admin password
# ══════════════════════════════════════════════════════════════════
log_step "Admin Panel Security"

CURRENT_PW=$(grep "^ADMIN_PASSWORD=" .env | cut -d'=' -f2)
if [[ "$CURRENT_PW" == "change-me-to-a-secure-password" ]] || [[ "$CURRENT_PW" == "admin123" ]] || [[ -z "$CURRENT_PW" ]]; then
    echo ""
    read -r -p "  Set admin panel password (or press Enter for default 'admin123'): " ADMIN_PW

    ADMIN_PW=${ADMIN_PW:-admin123}
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s|^ADMIN_PASSWORD=.*|ADMIN_PASSWORD=${ADMIN_PW}|" .env
    else
        sed -i "s|^ADMIN_PASSWORD=.*|ADMIN_PASSWORD=${ADMIN_PW}|" .env
    fi
    log_success "Admin password set"
fi

# ══════════════════════════════════════════════════════════════════
# STEP 6: Set file permissions
# ══════════════════════════════════════════════════════════════════
log_step "Setting file permissions"

chmod 600 .env
log_success ".env protected (600)"

if [ -d "scripts/" ]; then
    chmod +x scripts/*.sh 2>/dev/null || true
    log_success "Scripts made executable"
fi

# ══════════════════════════════════════════════════════════════════
# STEP 7: Build and start containers
# ══════════════════════════════════════════════════════════════════
log_step "Building Docker containers"

echo ""
read -r -p "  Start the application now? [Y/n]: " START_NOW
START_NOW=${START_NOW:-Y}

if [[ "${START_NOW,,}" == "y" ]]; then
    log_info "Building containers (this may take 2–5 minutes on first run)…"
    docker compose up -d --build

    log_info "Waiting for services to start…"
    sleep 15

    # Health check
    MAX_RETRIES=10
    RETRY=0
    while [ $RETRY -lt $MAX_RETRIES ]; do
        if curl -sf http://localhost:8000/health &>/dev/null; then
            break
        fi
        RETRY=$((RETRY + 1))
        log_info "Waiting for backend… (${RETRY}/${MAX_RETRIES})"
        sleep 5
    done

    if curl -sf http://localhost:8000/health &>/dev/null; then
        log_success "Backend is running!"
    else
        log_warn "Backend health check timed out — it may still be starting"
        log_info "Check logs with: docker compose logs backend"
    fi
else
    echo ""
    log_info "Run when ready: docker compose up -d --build"
fi

# ══════════════════════════════════════════════════════════════════
# DONE
# ══════════════════════════════════════════════════════════════════
echo ""
echo -e "${BOLD}${GREEN}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                    🎉 Setup Complete!                    ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"

echo ""
echo -e "${BOLD}  Next Steps:${NC}"
echo ""
echo -e "  1. ${YELLOW}Add documents${NC} to the documents/ folder:"
echo "     cp your-files/*.pdf documents/"
echo ""
echo -e "  2. ${YELLOW}Open the chat interface:${NC}"
echo "     http://localhost"
echo ""
echo -e "  3. ${YELLOW}Open the admin panel:${NC}"
echo "     http://localhost/admin.html"
echo ""
echo -e "  4. ${YELLOW}View API documentation:${NC}"
echo "     http://localhost/docs"
echo ""
echo -e "  5. ${YELLOW}View logs:${NC}"
echo "     docker compose logs -f backend"
echo ""
echo -e "  ${BLUE}For deployment help: see DEPLOYMENT.md${NC}"
echo -e "  ${BLUE}For troubleshooting: see TROUBLESHOOTING.md${NC}"
echo ""
