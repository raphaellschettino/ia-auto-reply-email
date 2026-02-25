import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Caminho base dos arquivos de conhecimento
BASE = "know"

def carregar_arquivo(nome):
    caminho = os.path.join(BASE, nome)
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def gerar_resposta_ia(texto_email: str) -> str:
    # 🔥 Carregar bases
    texto_precos = carregar_arquivo("precos.txt")
    texto_qualidade = carregar_arquivo("qualidade.txt")
    texto_politicas = carregar_arquivo("politicas.txt")

    prompt = f"""
Você é um atendente profissional e cordial.

USE EXCLUSIVAMENTE as informações abaixo para responder o cliente:

=== INFORMAÇÕES SOBRE PREÇOS ===
{texto_precos}

=== INFORMAÇÕES SOBRE QUALIDADE ===
{texto_qualidade}

=== POLÍTICAS OFICIAIS ===
{texto_politicas}

Agora, responda o e-mail do cliente de forma clara e educada:

E-MAIL DO CLIENTE:
{texto_email}

RESPOSTA:
"""

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return resposta.choices[0].message.content
