"""
backend/app/services/form_service.py
Form service: loads form definitions, validates submissions, sends email notifications.
"""

from __future__ import annotations

import json
import uuid
import asyncio
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import re

from app.utils.logger import logger
from app.utils.config import get_settings


FORMS_DIR = Path(__file__).parent.parent.parent / "forms"


class FormService:
    """
    Handles form definition loading, submission validation,
    storage, and email notification.
    """

    def __init__(self) -> None:
        self.settings = get_settings()
        self._form_cache: Dict[str, Dict[str, Any]] = {}
        self._load_all_forms()

    def _load_all_forms(self) -> None:
        """Load all form definition JSON files into cache."""
        if not FORMS_DIR.exists():
            logger.warning(f"Forms directory not found: {FORMS_DIR}")
            return

        for file_path in FORMS_DIR.glob("*.json"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    form_def = json.load(f)
                form_id = form_def.get("id")
                if form_id:
                    self._form_cache[form_id] = form_def
                    logger.info(f"Loaded form definition: {form_id}")
            except Exception as e:
                logger.error(f"Failed to load form {file_path.name}: {e}")

        logger.info(f"Loaded {len(self._form_cache)} form definitions")

    def get_form(self, form_id: str) -> Optional[Dict[str, Any]]:
        """Return a form definition by ID."""
        return self._form_cache.get(form_id)

    def list_forms(self) -> List[Dict[str, str]]:
        """Return a list of all available forms (summary only)."""
        return [
            {
                "id": form["id"],
                "title": form["title"],
                "description": form.get("description", ""),
            }
            for form in self._form_cache.values()
        ]

    def validate_submission(self, form_id: str, data: Dict[str, Any]) -> List[str]:
        """
        Validate submitted form data against the form definition.
        Returns a list of error messages (empty if valid).
        """
        errors = []
        form_def = self.get_form(form_id)
        if not form_def:
            return ["Invalid form ID"]

        fields = form_def.get("fields", [])
        for field in fields:
            if not field.get("required", False):
                continue

            field_name = field["name"]
            value = data.get(field_name)

            if value is None or (isinstance(value, str) and value.strip() == ""):
                errors.append(f"{field['label']} is required")
                continue

            field_type = field.get("type", "text")
            if field_type == "email" and value:
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', str(value)):
                    errors.append(f"{field['label']} must be a valid email address")

            elif field_type == "tel" and value:
                digits = re.sub(r'\D', '', str(value))
                if len(digits) < 10:
                    errors.append(f"{field['label']} must have at least 10 digits")

            elif field_type == "number" and value:
                try:
                    float(value)
                except (ValueError, TypeError):
                    errors.append(f"{field['label']} must be a number")

            elif field_type == "checkbox" and field.get("required"):
                if not value:
                    errors.append(f"{field['label']} must be accepted")

        if data.get("_gotcha"):
            errors.append("Spam detected")

        return errors

    async def process_submission(
        self,
        form_id: str,
        data: Dict[str, Any],
        session_id: Optional[str] = None,
        client_ip: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Process a form submission:
        1. Validate
        2. Store in database
        3. Send email notification
        4. Return confirmation
        """
        form_def = self.get_form(form_id)
        if not form_def:
            return {"success": False, "errors": ["Form not found"]}

        errors = self.validate_submission(form_id, data)
        if errors:
            return {"success": False, "errors": errors}

        submission_id = str(uuid.uuid4())
        submission_data = {
            "id": submission_id,
            "form_id": form_id,
            "form_title": form_def.get("title", "Unknown"),
            "data": data,
            "session_id": session_id,
            "client_ip": client_ip,
            "submitted_at": datetime.utcnow().isoformat(),
        }

        from app.services.database import get_db
        db = get_db()
        await db.save_form_submission(submission_data)

        asyncio.create_task(self._send_email_notification(submission_data))

        logger.info(
            f"Form submission received: {form_id} "
            f"from session={session_id[:8] if session_id else 'N/A'} "
            f"submission_id={submission_id}"
        )

        return {
            "success": True,
            "submission_id": submission_id,
            "message": (
                "Thank you! We've received your request and one of our team members "
                "will contact you shortly."
            ),
        }

    async def _send_email_notification(self, submission: Dict[str, Any]) -> None:
        """Send email notification for a form submission."""
        settings = self.settings

        notify_email = getattr(settings, 'notification_email', None)
        smtp_host = getattr(settings, 'smtp_host', None)

        if not notify_email:
            logger.info("No notification email configured — skipping email")
            return

        form_id = submission["form_id"]
        form_title = submission["form_title"]
        data = submission["data"]
        submitted_at = submission.get("submitted_at", "")

        subject = f"[{settings.business_name}] New {form_title} — {form_id}"

        fields_html = ""
        for key, value in data.items():
            if key.startswith("_"):
                continue
            label = key.replace("_", " ").title()
            display_value = "Yes" if value is True else ("" if value is False else str(value))
            fields_html += f"<tr><td style='padding:8px;border-bottom:1px solid #eee;font-weight:600;'>{label}</td><td style='padding:8px;border-bottom:1px solid #eee;'>{display_value}</td></tr>\n"

        html_body = f"""
        <html>
        <body style="font-family:Arial,sans-serif;color:#333;line-height:1.6;">
            <div style="max-width:600px;margin:0 auto;padding:20px;">
                <div style="background:#FCE300;padding:20px;text-align:center;border-radius:8px 8px 0 0;">
                    <h2 style="color:#000;margin:0;font-size:1.4rem;">New {form_title}</h2>
                    <p style="color:#333;margin:5px 0 0;">{settings.business_name} Chatbot</p>
                </div>
                <div style="background:#fff;padding:20px;border:1px solid #ddd;border-top:none;">
                    <p style="color:#666;font-size:0.9rem;">Received: {submitted_at}</p>
                    <table style="width:100%;border-collapse:collapse;margin-top:15px;font-size:0.95rem;">
                        {fields_html}
                    </table>
                    <div style="margin-top:25px;padding-top:20px;border-top:2px solid #FCE300;">
                        <p style="font-size:0.85rem;color:#888;">
                            Submission ID: {submission["id"]}<br>
                            Session: {submission.get("session_id", "N/A")}<br>
                            Source: Tori Chatbot
                        </p>
                    </div>
                </div>
                <div style="background:#f5f5f5;padding:15px;text-align:center;border-radius:0 0 8px 8px;font-size:0.8rem;color:#888;">
                    This is an automated notification from {settings.business_name} Chatbot
                </div>
            </div>
        </body>
        </html>
        """

        text_body = f"New {form_title} from {settings.business_name} Chatbot\n\n"
        for key, value in data.items():
            if key.startswith("_"):
                continue
            label = key.replace("_", " ").title()
            display_value = "Yes" if value is True else ("" if value is False else str(value))
            text_body += f"{label}: {display_value}\n"
        text_body += f"\nSubmission ID: {submission['id']}\n"
        text_body += f"Session: {submission.get('session_id', 'N/A')}\n"

        if smtp_host:
            try:
                await self._send_smtp_email(subject, html_body, text_body)
            except Exception as e:
                logger.error(f"Failed to send email notification: {e}")
        else:
            logger.info(f"Form submission email would be sent to {notify_email}")
            logger.info(f"Subject: {subject}")
            logger.info(f"Content preview:\n{text_body[:500]}")

    async def _send_smtp_email(self, subject: str, html_body: str, text_body: str) -> None:
        """Send email via SMTP."""
        settings = self.settings
        smtp_host = getattr(settings, 'smtp_host', '')
        smtp_port = getattr(settings, 'smtp_port', 587)
        smtp_user = getattr(settings, 'smtp_user', '')
        smtp_password = getattr(settings, 'smtp_password', '')
        smtp_from = getattr(settings, 'smtp_from', smtp_user)
        notify_email = getattr(settings, 'notification_email', '')

        if not all([smtp_host, smtp_user, smtp_password]):
            logger.warning("SMTP not fully configured")
            return

        import aiosmtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = smtp_from
        msg["To"] = notify_email

        msg.attach(MIMEText(text_body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        await aiosmtplib.send(
            msg,
            hostname=smtp_host,
            port=smtp_port,
            username=smtp_user,
            password=smtp_password,
            start_tls=True,
        )

        logger.info(f"Email notification sent to {notify_email}")


_form_service: Optional[FormService] = None


def get_form_service() -> FormService:
    global _form_service
    if _form_service is None:
        _form_service = FormService()
    return _form_service