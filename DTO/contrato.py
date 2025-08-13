from pydantic import BaseModel

class Contrato(BaseModel):
    empresa_id: str
    descricao: str
    valor: float