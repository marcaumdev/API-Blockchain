from pydantic import BaseModel

class Contrato(BaseModel):
    destinatario_cnpj: str
    descricao: str
    tipo: str
    valor: float