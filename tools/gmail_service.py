from googleapiclient.discovery import build
from utils.gmail_auth import get_gmail_credentials

def get_gmail_service():
    creds = get_gmail_credentials()
    service = build("gmail", "v1", credentials=creds)
    return service