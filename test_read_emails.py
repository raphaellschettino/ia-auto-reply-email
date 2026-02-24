from agentes.gmail_reader_agent import ler_emails_nao_lidos

emails = ler_emails_nao_lidos()
for email in emails:
    print("-"*50)
    print("FROM:", email.get("from"))
    print("SUBJECT:", email.get("subject"))
    print("BODY:", email.get("body"))