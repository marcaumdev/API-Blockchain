# models.py
from pydantic import BaseModel

class EmpresaInput(BaseModel):
    nome: str
    saldo_inicial: float = 0

class TransacaoInput(BaseModel):
    remetente_id: str
    destinatario_id: str
    valor: float

class ContratoInput(BaseModel):
    empresa_id: str
    descricao: str
    valor: float
