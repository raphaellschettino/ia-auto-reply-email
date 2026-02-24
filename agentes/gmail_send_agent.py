from email.mime.text import MIMEText
import base64
from tools.gmail_service import get_gmail_service

def enviar_email(destinatario, assunto, corpo):
    service = get_gmail_service()

    mensagem = MIMEText(corpo)
    mensagem["to"] = destinatario
    mensagem["subject"] = assunto

    raw = base64.urlsafe_b64encode(mensagem.as_bytes()).decode()

    retorno = service.users().messages().send(
        userId="me",
        body={"raw": raw}
    ).execute()

    return retorno