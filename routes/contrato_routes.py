from fastapi import APIRouter, Depends, HTTPException
from DTO import Contrato
from services import Contrato_Service
from services import autenticacao

router = APIRouter(prefix="/contrato", tags=["Contratos"])
contrato_service = Contrato_Service()

@router.post("", dependencies=[Depends(autenticacao)])
def criar_contrato(dados: Contrato):
    try:
        contrato = contrato_service.criar_contrato(dados)
        return {"message": "Contrato enviado para fila de aprovação", "contrato": contrato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
