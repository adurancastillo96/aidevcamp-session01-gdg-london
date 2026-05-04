"""Email agent sub-agent for sending travel itinerary emails via Gmail.

IMPORTANT: The Gmail API must be enabled in your GCP project (gemini-agent-mirror).
If not already enabled, visit:
https://console.cloud.google.com/apis/library/gmail.googleapis.com

On first use, an OAuth consent flow will open in the browser to authorize Gmail access.
The token is then cached in travel_planner_agent/gmail_token.json for future runs.
"""

import base64
import json
from email.mime.text import MIMEText
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from google.adk.agents import Agent
from google.adk.tools import FunctionTool
#from google.adk.tools.google_api_tool import GmailToolset

# ── OAuth configuration ────────────────────────────────────────────────────
_SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
_CREDENTIALS_PATH = Path(__file__).resolve().parent.parent / "credentials.json"
_TOKEN_PATH = Path(__file__).resolve().parent.parent / "gmail_token.json"


def _get_gmail_service():
    """Return an authenticated Gmail API service, refreshing/creating the token as needed."""
    creds = None

    # Load cached token if it exists
    if _TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(_TOKEN_PATH), _SCOPES)

    # Refresh expired token or run the OAuth flow for the first time
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(_CREDENTIALS_PATH), _SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Persist the token for the next run
        _TOKEN_PATH.write_text(creds.to_json())

    return build("gmail", "v1", credentials=creds)


# ── Send-email tool ────────────────────────────────────────────────────────

def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email via Gmail using the authenticated user's account.

    Args:
        to: Recipient email address (e.g. "user@example.com").
        subject: Email subject line.
        body: Plain-text body of the email.

    Returns:
        A dict with 'status' ('success' or 'error') and either 'message_id'
        or 'error_message'.
    """
    try:
        service = _get_gmail_service()

        # Build an RFC 2822 message
        mime_message = MIMEText(body, "plain", "utf-8")
        mime_message["To"] = to
        mime_message["Subject"] = subject

        # Base64url-encode the raw message (done in Python, not by the LLM)
        raw = base64.urlsafe_b64encode(mime_message.as_bytes()).decode("ascii")

        sent = service.users().messages().send(
            userId="me", body={"raw": raw}
        ).execute()

        return {
            "status": "success",
            "message_id": sent.get("id"),
            "detail": f"Email sent successfully to {to}.",
        }

    except Exception as exc:
        return {
            "status": "error",
            "error_message": str(exc),
        }


# Wrap the function so ADK can expose it to the LLM
send_email_tool = FunctionTool(func=send_email)

# ── Agent definition ───────────────────────────────────────────────────────

email_agent = Agent(
    name="email_agent",
    model="gemini-2.5-flash",
    description="Sends travel itinerary emails via Gmail on behalf of the user.",
    tools=[send_email_tool],
    instruction="""
You are an email assistant specialized in sending travel itineraries.

Your job:
- Compose a well-formatted plain-text email with the travel itinerary details.
- Send it using the send_email tool.

How to use send_email:
- to: the recipient's email address (ask the user if not provided).
- subject: a clear subject like "Your Travel Itinerary: [Destination]".
- body: the full itinerary in plain text. Include all days, activities, and notes.

Rules:
- Always ask for the recipient email address if not provided.
- Do NOT write Python code or import statements — just call send_email with the three parameters.
- After sending, confirm with the message ID returned by the tool.
- If the tool returns an error, report it clearly to the user.
""",
)
