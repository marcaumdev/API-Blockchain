from fastapi import APIRouter, HTTPException
from services import Empresa_Service
from models import Blockchain
from DTO import Transacao
from services import Transacao_Service, Fila_Service

router = APIRouter(prefix="/transacao", tags=["Transações"])
transacao_service = Transacao_Service()
fila_service = Fila_Service()

@router.post("")
def criar_transacao(dados: Transacao):
    try:
        transacao = transacao_service.criar_transacao(dados)
        return {"message": "Transação enviada para fila de aprovação", "transacao": transacao}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/fila")
def listar_fila_transacoes():
    return fila_service.listar_fila("transacoes")

@router.post("/aprovar/{transacao_id}")
def aprovar_transacao(transacao_id: str):
    try:
        bloco = fila_service.aprovar_item(transacao_id, tipo="transacao")
        return {"message": "Transação aprovada e adicionada à blockchain", "bloco": bloco}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))