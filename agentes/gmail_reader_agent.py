import base64
from tools.gmail_service import get_gmail_service

def ler_emails_nao_lidos():
    service = get_gmail_service()

    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX', 'UNREAD']
    ).execute()

    mensagens = results.get('messages', [])

    emails = []

    for msg in mensagens:
        msg_data = service.users().messages().get(
            userId='me',
            id=msg['id'],
            format='full'
        ).execute()

        payload = msg_data['payload']
        headers = payload.get("headers", [])

        remetente = next((h["value"] for h in headers if h["name"] == "From"), "desconhecido")
        assunto = next((h["value"] for h in headers if h["name"] == "Subject"), "")
        
        partes = payload.get("parts", [])
        corpo = ""

        for parte in partes:
            if parte.get("mimeType") == "text/plain":
                corpo = base64.urlsafe_b64decode(parte["body"]["data"]).decode()

        emails.append({
            "id": msg["id"],
            "from": remetente,
            "subject": assunto,
            "body": corpo
        })

    return emails