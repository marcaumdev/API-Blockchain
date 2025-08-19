from pydantic import BaseModel

class Transacao(BaseModel):
    remetente_id: str
    destinatario_id: str
    descricao: str
    valor: float