from pydantic import BaseModel, EmailStr

class EnviarEmailSchema(BaseModel):
    destinatario: EmailStr
    assunto: str
    corpo: str