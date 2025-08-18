from pydantic import BaseModel

class Atualizar_Saldo(BaseModel):
    cnpj: int
    valor: float