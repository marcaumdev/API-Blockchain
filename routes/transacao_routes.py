from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from DTO import Transacao
from services import Transacao_Service, Fila_Service
from services import autenticacao

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