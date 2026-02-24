from fastapi import APIRouter
from agentes.auto_reply_agent import processar_respostas_automaticas

router = APIRouter()

@router.post("/auto-reply")
def auto_reply():
    return processar_respostas_automaticas()