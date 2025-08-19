# empresa.py
from models import Empresa
from storage import salvar_json, carregar_json, excluir_registro
import bcrypt
import jwt
from datetime import datetime, timedelta

ARQUIVO_EMPRESAS = "storage/empresas.json"
SECRET_KEY = "BlockchainAPISecretKey"

class Empresa_Service:

    def __init__(self):
        self.empresas = carregar_json(ARQUIVO_EMPRESAS)

    def salvar(self):
        salvar_json(ARQUIVO_EMPRESAS, self.empresas)

    def listar(self):
        return self.empresas

    def criar_empresa(self, razao_social, nome_fantasia, cnpj, tipo, senha):

        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

        empresa = Empresa(razao_social, nome_fantasia, cnpj, tipo, senha_hash)
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

    def autenticar_empresa(self, cnpj, senha):
        usuario = next((u for u in self.empresas if u["cnpj"] == cnpj), None)
        if usuario and bcrypt.checkpw(senha.encode(), usuario["senha_hash"].encode()):
            return usuario
        return None

    def criar_token(usuario):
        payload = {
            "sub": usuario["username"],
            "tipo": usuario["tipo"],
            "exp": datetime.utcnow() + timedelta(hours=12)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")