from fastapi import APIRouter
from services import Empresa_Service
from DTO import Empresa

router = APIRouter(prefix="/empresa", tags=["Empresas"])
empresas_service = Empresa_Service()

@router.post("")
def criar_empresa(dados: Empresa):
    return empresas_service.criar_empresa(dados.nome, dados.saldo_inicial)

@router.get("")
def listar_empresas():
    return empresas_service.listar()
