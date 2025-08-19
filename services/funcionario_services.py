from storage import carregar_json, salvar_json
from services import Empresa_Service
from models import Funcionario

ARQUIVO_FUNCIONARIOS = "storage/funcionarios.json"

class Funcionario_Service:
    def __init__(self):
        self.funcionarios = carregar_json(ARQUIVO_FUNCIONARIOS) or []
        self.empresas_service = Empresa_Service()

    def salvar(self):
        salvar_json(ARQUIVO_FUNCIONARIOS, self.funcionarios)

    def listar(self):
        return self.funcionarios

    def buscar_por_id(self, funcionario_id: int):
        for f in self.funcionarios:
            if f["id"] == funcionario_id:
                return f
        return None

    def criar(self, nome: str, cnpj_empresa: int):
        # Verificar se empresa existe pelo CNPJ
        empresa = self.empresas_service.buscar_por_cnpj(Funcionario.cnpj_empresa)
        if not empresa:
            return None  # Empresa não encontrada

        funcionario = Funcionario(cnpj_empresa=cnpj_empresa, nome=nome, cargo=Funcionario.cargo)
        self.funcionarios.append(funcionario.dict())
        self.salvar()
        return funcionario.dict()

    def atualizar(self, funcionario_id: int, nome: str, cnpj_empresa: int):
        for f in self.funcionarios:
            dados = Funcionario(nome=nome, cnpj_empresa=cnpj_empresa)
            if f["id"] == funcionario_id:
                f.update(dados.dict(exclude_unset=True))
                self.salvar()
                return f
        return None

    def excluir(self, funcionario_id: int):
        for f in self.funcionarios:
            if f["id"] == funcionario_id:
                self.funcionarios.remove(f)
                self.salvar()
                return True
        return False
