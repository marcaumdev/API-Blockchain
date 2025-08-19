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
            "tipo": tipo,      # "transacao" ou "contrato"
            "dados": dados,
            "status": "PENDENTE"
        }
        self.fila.append(item)
        self.salvar()
        return item

    def listar_fila(self):
        """
        Retorna todos os itens pendentes na fila.
        """
        return [item for item in self.fila if item["status"] == "PENDENTE"]

    def aprovar_item(self, index):
        """
        Aprova um item específico da fila (por índice).
        O item é adicionado à blockchain e marcado como 'APROVADO'.
        """
        if index < 0 or index >= len(self.fila):
            return {"erro": "Índice inválido"}

        item = self.fila[index]
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

    def rejeitar_item(self, index):
        """
        Rejeita um item da fila.
        """
        if index < 0 or index >= len(self.fila):
            return {"erro": "Índice inválido"}

        item = self.fila[index]
        if item["status"] != "PENDENTE":
            return {"erro": "Item já processado"}

        item["status"] = "REJEITADO"
        self.salvar()
        return item
