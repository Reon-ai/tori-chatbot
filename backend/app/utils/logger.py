"""
backend/app/utils/logger.py
Structured logging setup for the entire backend.
"""

import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "rag_chatbot",
    level: str = "INFO",
    log_file: Optional[str] = "./data/logs/app.log",
) -> logging.Logger:
    """
    Create and configure a named logger.
    - Outputs JSON-friendly format to stdout
    - Rotates log file at 10 MB, keeps 5 backups
    """
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    if logger.handlers:
        return logger  # Already configured

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    # ── Stdout handler ────────────────────────────────────────
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(numeric_level)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    # ── File handler ──────────────────────────────────────────
    if log_file:
        try:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = RotatingFileHandler(
                log_path,
                maxBytes=10 * 1024 * 1024,  # 10 MB
                backupCount=5,
                encoding="utf-8",
            )
            file_handler.setLevel(numeric_level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            logger.warning(f"Could not create file logger: {e}")

    logger.propagate = False
    return logger


# Default application logger
logger = setup_logger()
