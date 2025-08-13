# empresa.py
from models import Empresa
from storage import salvar_json, carregar_json

ARQUIVO_EMPRESAS = "empresas.json"

class Empresa_Service:
    def __init__(self):
        self.empresas = carregar_json(ARQUIVO_EMPRESAS)

    def salvar(self):
        salvar_json(ARQUIVO_EMPRESAS, self.empresas)

    def listar(self):
        return self.empresas

    def criar_empresa(self, nome, saldo_inicial=0):
        empresa = Empresa(nome, saldo_inicial)
        self.empresas.append(empresa.to_dict())
        self.salvar()
        return empresa.to_dict()

    def buscar_por_id(self, empresa_id):
        for e in self.empresas:
            if e["id"] == empresa_id:
                return e
        return None

    def atualizar_saldo(self, empresa_id, valor):
        for e in self.empresas:
            if e["id"] == empresa_id:
                e["saldo"] += valor
                self.salvar()
                return e
        return None
