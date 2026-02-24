from agentes.gmail_reader_agent import ler_emails_nao_lidos
from agentes.gmail_reply_agent import gerar_resposta_ia
from agentes.gmail_send_agent import enviar_email
from tools.gmail_service import get_gmail_service

def processar_respostas_automaticas():
    emails = ler_emails_nao_lidos()

    if not emails:
        return {"status": "nenhum email novo"}

    enviados = 0
    service = get_gmail_service()

    for email in emails:
        assunto = email["subject"]

        # FILTRO DO USUÁRIO
        if "[Filtro teste]" not in assunto:
            continue

        remetente = email["from"]
        texto = email["body"]

        resposta = gerar_resposta_ia(texto)
        enviar_email(destinatario=remetente, assunto=f"Re: {assunto}", corpo=resposta)

        # 🔥 MARCAR COMO LIDO
        service.users().messages().modify(
            userId="me",
            id=email["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        enviados += 1

    return {"status": "respostas enviadas", "quantidade": enviados}