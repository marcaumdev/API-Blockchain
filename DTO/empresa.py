from pydantic import BaseModel

class Empresa(BaseModel):
    nome: str
    saldo: float = 0