# funcionario.py
import uuid

class Funcionario:
    def __init__(self, nome, cnpj_empresa):
        self.id = str(uuid.uuid4())  # Gera ID único
        self.nome = nome
        self.cnpj_empresa = cnpj_empresa

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "cnpj_empresa": self.cnpj_empresa}
