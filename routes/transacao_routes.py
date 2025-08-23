from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from DTO import Transacao
from services import Transacao_Service, Fila_Service
from services import somente_governo, autenticacao

router = APIRouter(prefix="/transacao", tags=["Transações"])
transacao_service = Transacao_Service()
fila_service = Fila_Service()

@router.post("", dependencies=[Depends(autenticacao)])
def criar_transacao(dados: Transacao):
    try:
        transacao = transacao_service.criar_transacao(dados)
        return {"message": "Transação enviada para fila de aprovação", "transacao": transacao}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/fila", dependencies=[Depends(autenticacao)])
def listar_fila_transacoes():
    return fila_service.listar_fila("transacao")

@router.post("/aprovar/{transacao_id}", dependencies=[Depends(somente_governo)])
def aprovar_transacao(transacao_id: str):
    try:
        bloco = fila_service.aprovar_item(transacao_id, tipo="transacao")
        return {"message": "Transação aprovada e adicionada à blockchain", "bloco": bloco}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))