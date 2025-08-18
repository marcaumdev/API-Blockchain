# empresa.py
from models import Empresa
from storage import salvar_json, carregar_json, excluir_registro

ARQUIVO_EMPRESAS = "storage/empresas.json"

class Empresa_Service:
    def __init__(self):
        self.empresas = carregar_json(ARQUIVO_EMPRESAS)

    def salvar(self):
        salvar_json(ARQUIVO_EMPRESAS, self.empresas)

    def listar(self):
        return self.empresas

    def criar_empresa(self, razao_social, nome_fantasia, cnpj, tipo, senha):
        empresa = Empresa(razao_social, nome_fantasia, cnpj, tipo, senha)
        self.empresas.append(empresa.to_dict())
        self.salvar()
        return empresa.to_dict()

    def buscar_por_id(self, empresa_id):
        for e in self.empresas:
            if e["id"] == empresa_id:
                return e
        return None
    
    def buscar_por_cnpj(self, cnpj):
        for e in self.empresas:
            if e["cnpj"] == cnpj:
                return e
        return None

    def atualizar_saldo(self, cnpj, valor):
        for e in self.empresas:
            if e["cnpj"] == cnpj:
                e["saldo"] += valor
                self.salvar()
                return e
        return None
    
    def excluir_empresa_por_cnpj(self, cnpj):
        return excluir_registro(ARQUIVO_EMPRESAS, "cnpj", cnpj)
