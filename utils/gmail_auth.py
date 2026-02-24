from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify"
]

def get_gmail_credentials():
    creds = None

    if os.path.exists("utils/token.json"):
        creds = Credentials.from_authorized_user_file("utils/token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "utils/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("utils/token.json", "w") as token:
            token.write(creds.to_json())

    return creds
