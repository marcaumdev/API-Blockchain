from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from services import Funcionario_Service
from DTO import Funcionario
from services import autenticacao, somente_governo

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])
service = Funcionario_Service()

@router.get("", dependencies=[Depends(autenticacao)])
def listar_funcionarios():
    return service.listar()

@router.get("/{funcionario_id}", dependencies=[Depends(autenticacao)])
def buscar_funcionario(funcionario_id: int):
    funcionario = service.buscar_por_id(funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.post("", dependencies=[Depends(somente_governo)])
def criar_funcionario(dados: Funcionario):
    funcionario = service.criar(dados.nome, dados.cnpj_empresa)
    if not funcionario:
        raise HTTPException(status_code=400, detail="Empresa não encontrada para o CNPJ informado")
    return funcionario

@router.put("/{funcionario_id}", dependencies=[Depends(somente_governo)])
def atualizar_funcionario(funcionario_id: int, dados: Funcionario):
    funcionario = service.atualizar(funcionario_id, dados.nome, dados.cnpj_empresa)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.delete("/{funcionario_id}", dependencies=[Depends(somente_governo)] )
def excluir_funcionario(funcionario_id: int):
    sucesso = service.excluir(funcionario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return {"mensagem": "Funcionário excluído com sucesso"}
