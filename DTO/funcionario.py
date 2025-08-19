from pydantic import BaseModel

class Funcionario(BaseModel):
    nome: str
    cnpj: int