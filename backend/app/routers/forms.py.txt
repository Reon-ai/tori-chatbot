"""
backend/app/routers/forms.py
Form API endpoints.
GET  /api/forms              — list all available forms
GET  /api/forms/{form_id}    — get a specific form definition
POST /api/forms/submit       — submit a completed form
GET  /api/forms/submissions  — list form submissions (admin)
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.models.schemas import (
    FormDefinition, FormDefinitionSummary,
    FormSubmitRequest, FormSubmitResponse,
)
from app.services.form_service import get_form_service, FormService
from app.services.database import get_db, Database
from app.routers.admin import require_admin
from app.utils.logger import logger

router = APIRouter(prefix="/api/forms", tags=["forms"])


@router.get("")
async def list_forms(
    form_service: FormService = Depends(get_form_service),
) -> List[FormDefinitionSummary]:
    """Return a list of all available form definitions."""
    forms = form_service.list_forms()
    return [FormDefinitionSummary(**f) for f in forms]


@router.get("/{form_id}", response_model=FormDefinition)
async def get_form(
    form_id: str,
    form_service: FormService = Depends(get_form_service),
) -> FormDefinition:
    """Return a specific form definition by ID."""
    form_def = form_service.get_form(form_id)
    if not form_def:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Form '{form_id}' not found.",
        )
    return FormDefinition(**form_def)


@router.post("/submit", response_model=FormSubmitResponse)
async def submit_form(
    request: Request,
    payload: FormSubmitRequest,
    form_service: FormService = Depends(get_form_service),
) -> FormSubmitResponse:
    """
    Submit a completed form.
    Validates the data, stores the submission, and triggers email notification.
    """
    client_ip = request.client.host if request.client else "unknown"

    result = await form_service.process_submission(
        form_id=payload.form_id,
        data=payload.data,
        session_id=payload.session_id,
        client_ip=client_ip,
    )

    if result["success"]:
        return FormSubmitResponse(
            success=True,
            submission_id=result.get("submission_id"),
            message=result["message"],
        )
    else:
        return FormSubmitResponse(
            success=False,
            errors=result.get("errors", ["Submission failed"]),
        )


@router.get(
    "/submissions/all",
    dependencies=[Depends(require_admin)],
)
async def list_submissions(
    form_id: Optional[str] = None,
    limit: int = 50,
    db: Database = Depends(get_db),
) -> Dict[str, Any]:
    """List form submissions (admin only)."""
    submissions = await db.list_form_submissions(form_id=form_id, limit=limit)
    return {"submissions": submissions, "total": len(submissions)}