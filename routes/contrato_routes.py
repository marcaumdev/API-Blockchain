from fastapi import APIRouter, Depends, HTTPException
from DTO import Contrato
from services import Contrato_Service, Fila_Service
from services import autenticacao, somente_governo

router = APIRouter(prefix="/contrato", tags=["Contratos"])
contrato_service = Contrato_Service()
fila_service = Fila_Service()

@router.post("", dependencies=[Depends(autenticacao)])
def criar_contrato(dados: Contrato):
    try:
        contrato = contrato_service.criar_contrato(dados)
        return {"message": "Contrato enviado para fila de aprovação", "contrato": contrato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/fila", dependencies=[Depends(autenticacao)])
def listar_fila_contratos():
    return fila_service.listar_fila("contrato")

@router.post("/aprovar/{contrato_id}", dependencies=[Depends(somente_governo)])
def aprovar_contrato(contrato_id: str):
    try:
        bloco = fila_service.aprovar_item(contrato_id, tipo="contrato")
        return {"message": "Contrato aprovado e adicionado à blockchain", "bloco": bloco}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
