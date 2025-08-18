# funcionario.py
import uuid

class Funcionario:
    def __init__(self, nome, id_empresa):
        self.id = str(uuid.uuid4())  # Gera ID único
        self.nome = nome
        self.id_empresa = id_empresa

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "id_empresa": self.id_empresa}
