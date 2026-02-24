import os
from dotenv import load_dotenv

# CARREGAR .ENV MANUALMENTE
ENV_PATH = r"C:\Users\rapha\OneDrive\Área de Trabalho\estudos-ia\api\.env"
load_dotenv(ENV_PATH)
print("MAIN.LOAD_OK =", os.getenv("OPENAI_API_KEY"))

from fastapi import FastAPI
from routes.auto_reply_route import router as auto_reply_router
from apscheduler.schedulers.background import BackgroundScheduler
from agentes.auto_reply_agent import processar_respostas_automaticas

app = FastAPI()

def job_auto_reply():
    resposta = processar_respostas_automaticas()
    print("Agente rodou:", resposta)

scheduler = BackgroundScheduler()
scheduler.add_job(job_auto_reply, "interval", minutes=1)
scheduler.start()

app.include_router(auto_reply_router, prefix="/gmail")