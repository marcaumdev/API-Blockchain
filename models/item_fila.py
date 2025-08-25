# empresa.py
import uuid

class Item_Fila:
    def __init__(self, tipo, status, dados):
        self.id = str(uuid.uuid4())  # Gera ID único
        self.tipo = tipo
        self.status = status
        self.dados = dados

    def to_dict(self):
        return {"id": self.id, "tipo": self.tipo, "status": self.status, "dados": self.dados}
