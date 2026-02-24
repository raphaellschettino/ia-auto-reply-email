import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resposta_ia(texto_email: str) -> str:
    prompt = f"""
Você é um assistente educado, profissional e direto.
Gere uma resposta clara, simples e respeitosa ao e-mail abaixo:

E-MAIL DO CLIENTE:
{texto_email}

Responda como se fosse um atendente humano.
"""

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.6
    )

    return resposta.choices[0].message.content