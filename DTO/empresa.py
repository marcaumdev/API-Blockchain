from pydantic import BaseModel

class Empresa(BaseModel):
    razao_social: str
    nome_fantasia: str
    cnpj: int
    tipo: str
    senha: str