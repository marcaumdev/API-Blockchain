from fastapi import APIRouter
from services import Empresa_Service
from DTO import Empresa, Atualizar_Saldo

router = APIRouter(prefix="/empresa", tags=["Empresas"])
empresas_service = Empresa_Service()

@router.get("")
def listar_empresas():
    return empresas_service.listar()

@router.get("/{id}")
def buscar_por_empresa_id(id):
    return empresas_service.buscar_por_id(id)

@router.get("/{cnpj}")
def buscar_por_empresa_cnpj(cnpj):
    return empresas_service.buscar_por_cnpj(cnpj)

@router.post("")
def criar_empresa(dados: Empresa):
    return empresas_service.criar_empresa(dados.razao_social, dados.nome_fantasia, dados.cnpj, dados.senha)

@router.put("")
def atualizar_saldo(dados: Atualizar_Saldo):
    return empresas_service.atualizar_saldo(dados.cnpj, dados.valor)

@router.delete("/{cnpj}")
def excluir_empresa_por_cnpj(cnpj):
    return empresas_service.excluir_empresa_por_cnpj(cnpj)