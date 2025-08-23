from fastapi import APIRouter, Depends
from services import Empresa_Service, autenticacao, somente_governo
from DTO import Empresa, Atualizar_Saldo

router = APIRouter(prefix="/empresa", tags=["Empresas"])
empresas_service = Empresa_Service()

@router.get("", dependencies=[Depends(autenticacao)])
def listar_empresas():
    return empresas_service.listar()

@router.get("/{id}", dependencies=[Depends(autenticacao)])
def buscar_por_empresa_id(id):
    return empresas_service.buscar_por_id(id)

@router.get("/{cnpj}", dependencies=[Depends(somente_governo)])
def buscar_por_empresa_cnpj(cnpj):
    return empresas_service.buscar_por_cnpj(cnpj)

@router.post("", dependencies=[Depends(somente_governo)])
def criar_empresa(dados: Empresa):
    return empresas_service.criar_empresa(dados.razao_social, dados.nome_fantasia, dados.cnpj, dados.tipo, dados.senha)

@router.put("", dependencies=[Depends(somente_governo)])
def atualizar_saldo(dados: Atualizar_Saldo):
    return empresas_service.atualizar_saldo(dados.cnpj, dados.valor)

@router.delete("/{cnpj}", dependencies=[Depends(somente_governo)])
def excluir_empresa_por_cnpj(cnpj):
    return empresas_service.excluir_empresa_por_cnpj(cnpj)