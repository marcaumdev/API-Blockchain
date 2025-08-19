from fastapi import APIRouter, HTTPException
from services import Empresa_Service
from models import Blockchain
from DTO import Contrato

router = APIRouter(prefix="/contrato", tags=["Contratos"])
empresas_service = Empresa_Service()
blockchain = Blockchain()

@router.post("")
def criar_contrato(dados: Contrato):
    empresa = empresas_service.buscar_por_id(dados.empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    blockchain.adicionar_bloco({
        "tipo": dados.tipo,
        "empresa": empresa["nome"],
        "descricao": dados.descricao,
        "valor": dados.valor
    })
    return {"mensagem": "Contrato registrado com sucesso"}
