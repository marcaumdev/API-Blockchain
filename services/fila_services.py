import uuid
from storage.storage import salvar_json, carregar_json
from models import Blockchain

ARQUIVO_FILA = "storage/fila.json"

class Fila_Service:
    def __init__(self):
        self.fila = carregar_json(ARQUIVO_FILA) or []
        self.blockchain = Blockchain()

    def salvar(self):
        salvar_json(ARQUIVO_FILA, self.fila)

    def adicionar_na_fila(self, tipo, dados):
        """
        Adiciona um item (transação ou contrato) na fila para aprovação.
        """
        item = {
            "id": str(uuid.uuid4()),  # id único
            "tipo": tipo,             # "transacao" ou "contrato"
            "dados": dados,
            "status": "PENDENTE"
        }
        self.fila.append(item)
        self.salvar()
        return item

    def listar_fila(self, tipo: str = None, incluir_rejeitados=False):
        """
        Retorna itens da fila (por tipo e status).
        - Se tipo=None, retorna todos.
        - Por padrão, retorna só pendentes, mas pode incluir rejeitados.
        """
        return [
            item for item in self.fila
            if (tipo is None or item["tipo"] == tipo)
            and (item["status"] == "PENDENTE" or (incluir_rejeitados and item["status"] == "REJEITADO"))
        ]

    def aprovar_item(self, item_id: str):
        """
        Aprova um item específico da fila (por id).
        O item é adicionado à blockchain e marcado como 'APROVADO'.
        """
        item = next((i for i in self.fila if i["id"] == item_id), None)
        if not item:
            return {"erro": "Item não encontrado"}

        if item["status"] != "PENDENTE":
            return {"erro": "Item já processado"}

        # cria bloco na blockchain
        self.blockchain.adicionar_bloco({
            "tipo": item["tipo"],
            "dados": item["dados"]
        })

        # atualiza status
        item["status"] = "APROVADO"
        self.salvar()
        return item

    def rejeitar_item(self, item_id: str):
        """
        Rejeita um item da fila (por id).
        """
        item = next((i for i in self.fila if i["id"] == item_id), None)
        if not item:
            return {"erro": "Item não encontrado"}

        if item["status"] != "PENDENTE":
            return {"erro": "Item já processado"}

        item["status"] = "REJEITADO"
        self.salvar()
        return item
