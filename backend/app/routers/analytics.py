"""
backend/app/routers/analytics.py
Analytics endpoints.
GET /api/admin/analytics — aggregated usage metrics
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter, Depends

from app.models.schemas import AnalyticsResponse, DailyStats, TopQuestion
from app.services.database import get_db, Database
from app.routers.admin    import require_admin

router = APIRouter(prefix="/api/admin", tags=["analytics"])


@router.get(
    "/analytics",
    response_model=AnalyticsResponse,
    dependencies=[Depends(require_admin)],
)
async def get_analytics(
    days: int = 30,
    db:   Database = Depends(get_db),
) -> AnalyticsResponse:
    """
    Return aggregated analytics for the last `days` days.
    Includes: daily query counts, response times, top questions,
    satisfaction rate, and document statistics.
    """
    data          = await db.get_analytics(days=days)
    total_docs    = await db.count_documents()
    total_chunks  = await db.count_chunks()

    daily = [
        DailyStats(
            date=d["date"],
            query_count=d["query_count"],
            avg_response_ms=d.get("avg_response_ms"),
            positive_ratings=d.get("positive_ratings", 0),
            negative_ratings=d.get("negative_ratings", 0),
        )
        for d in data.get("daily_stats", [])
    ]

    top_q = [
        TopQuestion(question=q["question"], count=q["count"])
        for q in data.get("top_questions", [])
    ]

    return AnalyticsResponse(
        total_queries=data["total_queries"],
        avg_response_time_ms=data.get("avg_response_time_ms"),
        satisfaction_rate=data.get("satisfaction_rate"),
        error_rate=data.get("error_rate", 0.0),
        daily_stats=daily,
        top_questions=top_q,
        total_documents=total_docs,
        total_chunks=total_chunks,
    )
