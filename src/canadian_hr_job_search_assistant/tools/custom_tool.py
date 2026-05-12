import os
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class ApplicationEmailInput(BaseModel):
    """Input schema for submitting an application by email."""

    recipient_email: str = Field(..., description="Employer or recruiter email address.")
    subject: str = Field(..., description="Application email subject line.")
    body: str = Field(..., description="Application email body.")
    resume_path: str | None = Field(
        default=None,
        description="Optional path to a resume file to attach. Uses RESUME_FILE_PATH if omitted.",
    )
    cover_letter_path: str | None = Field(
        default=None,
        description="Optional path to a cover letter file to attach.",
    )


class ApplicationEmailTool(BaseTool):
    name: str = "submit_application_email"
    description: str = (
        "Sends a real job application email when a posting provides a direct employer "
        "or recruiter email address. Do not use this for web portals."
    )
    args_schema: Type[BaseModel] = ApplicationEmailInput

    def _run(
        self,
        recipient_email: str,
        subject: str,
        body: str,
        resume_path: str | None = None,
        cover_letter_path: str | None = None,
    ) -> str:
        if os.getenv("APPLY_APPROVED", "").lower() != "true":
            return (
                "APPROVAL_REQUIRED: application email was prepared but not sent. "
                "Run the Approved Job Apply Automation workflow with approval=APPLY "
                "to send direct-email applications."
            )

        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", recipient_email.strip()):
            return f"SKIPPED: '{recipient_email}' is not a valid direct email address."

        sender_email = os.getenv("EMAIL_SENDER") or os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASSWORD", "")
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))

        if not sender_email or not sender_password:
            return "SKIPPED: EMAIL_USER/EMAIL_SENDER or EMAIL_PASSWORD is not configured."

        message = MIMEMultipart()
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email
        message.attach(MIMEText(body, "plain"))

        resolved_resume_path = resume_path or os.getenv("RESUME_FILE_PATH")
        if not resolved_resume_path:
            return "SKIPPED: RESUME_FILE_PATH is not configured, so no resume can be attached."

        attachment_paths = [
            resolved_resume_path,
            cover_letter_path,
        ]
        attached = []
        for attachment_path in [path for path in attachment_paths if path]:
            path = Path(attachment_path)
            if not path.exists():
                return f"SKIPPED: attachment not found: {path}"

            from email import encoders
            from email.mime.base import MIMEBase

            with path.open("rb") as attachment_file:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={path.name}",
            )
            message.attach(part)
            attached.append(path.name)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

        attachment_note = f" with attachments: {', '.join(attached)}" if attached else ""
        return f"SENT: application email sent to {recipient_email}{attachment_note}."
