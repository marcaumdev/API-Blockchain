from pydantic import BaseModel

class Transacao(BaseModel):
    remetente_id: str
    destinatario_id: str
    valor: float