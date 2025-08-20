from fastapi import APIRouter, HTTPException
from services import Empresa_Service
from models import Blockchain
from DTO import Contrato
from services import Contrato_Service, Fila_Service

router = APIRouter(prefix="/contrato", tags=["Contratos"])
contrato_service = Contrato_Service()
fila_service = Fila_Service()

@router.post("")
def criar_contrato(dados: Contrato):
    try:
        contrato = contrato_service.criar_contrato(dados)
        return {"message": "Contrato enviado para fila de aprovação", "contrato": contrato}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/fila")
def listar_fila_contratos():
    return fila_service.listar_fila("contratos")

@router.post("/aprovar/{contrato_id}")
def aprovar_contrato(contrato_id: str):
    try:
        bloco = fila_service.aprovar_item(contrato_id, tipo="contrato")
        return {"message": "Contrato aprovado e adicionado à blockchain", "bloco": bloco}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
