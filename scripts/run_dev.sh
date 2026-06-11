#!/usr/bin/env bash
# ================================================================
# scripts/run_dev.sh
# Start the development environment with hot-reload enabled.
# Usage: ./scripts/run_dev.sh
# ================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}${BLUE}"
echo "  🔧 Starting RAG Chatbot — Development Mode"
echo -e "${NC}"

# Check .env
if [ ! -f ".env" ]; then
    echo -e "${RED}ERROR: .env file not found. Run ./scripts/setup.sh first.${NC}"
    exit 1
fi

# Check OpenAI key
OPENAI_KEY=$(grep "^OPENAI_API_KEY=" .env | cut -d'=' -f2)
if [[ "$OPENAI_KEY" == "sk-your-openai-api-key-here" ]] || [[ -z "$OPENAI_KEY" ]]; then
    echo -e "${RED}WARNING: OPENAI_API_KEY not set in .env${NC}"
    echo "  The backend will start but responses will be unavailable."
fi

echo -e "${BLUE}ℹ  Starting with hot-reload enabled…${NC}"
echo ""
echo "  Backend:   http://localhost:8000"
echo "  Frontend:  http://localhost:3000"
echo "  API Docs:  http://localhost:8000/docs"
echo ""
echo "  Press Ctrl+C to stop"
echo ""

# Start with dev override
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
