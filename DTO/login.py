from pydantic import BaseModel

class Login(BaseModel):
    cnpj: str
    senha: str