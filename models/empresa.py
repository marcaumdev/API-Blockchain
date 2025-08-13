# empresa.py
import uuid

class Empresa:
    def __init__(self, nome, saldo_inicial=0):
        self.id = str(uuid.uuid4())  # Gera ID único
        self.nome = nome
        self.saldo = saldo_inicial

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "saldo": self.saldo}
