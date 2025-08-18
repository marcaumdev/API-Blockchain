# empresa.py
import uuid

class Empresa:
    def __init__(self, razao_social, nome_fantasia, cnpj, tipo, senha):
        self.id = str(uuid.uuid4())  # Gera ID único
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.saldo = 0
        self.tipo = tipo
        self.senha = senha

    def to_dict(self):
        return {"id": self.id, "razao social": self.razao_social, "nome fantasia": self.nome_fantasia, "cnpj": self.cnpj, "tipo": self.tipo,"senha": self.senha, "saldo": self.saldo }
