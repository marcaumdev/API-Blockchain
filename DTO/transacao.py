from pydantic import BaseModel

class Transacao(BaseModel):
    remetente_cnpj: str
    destinatario_cnpj: str
    descricao: str
    valor: float