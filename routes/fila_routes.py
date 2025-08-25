from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from services import Fila_Service
from services import somente_governo, autenticacao

router = APIRouter(prefix="/fila", tags=["Fila"])
fila_service = Fila_Service()

@router.get("/{tipo}", dependencies=[Depends(autenticacao)])
def listar_fila_transacoes(tipo:str = None):
    return fila_service.listar_fila(tipo)

@router.get("/rejeitados/{tipo}", dependencies=[Depends(autenticacao)])
def listar_fila_transacoes(tipo:str):
    return fila_service.listar_fila(tipo, True)

@router.post("/revisar/{item_id}", dependencies=[Depends(somente_governo)])
def aprovar_transacao(item_id: str, aprovado: bool):
    if(aprovado):
        try:
            bloco = fila_service.aprovar_item(item_id)
            return {"message": "Item aprovado e adicionado à blockchain", "bloco": bloco}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    else:
        try:
            bloco = fila_service.rejeitar_item(item_id)
            return {"message": "Item recusado e não foi adicionado à blockchain", "bloco": bloco}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))