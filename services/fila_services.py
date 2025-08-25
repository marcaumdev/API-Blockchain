import uuid
from services import Empresa_Service
from storage.storage import salvar_json, carregar_json
from models import Blockchain, Item_Fila

ARQUIVO_FILA = "storage/fila.json"
empresas_service = Empresa_Service()


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
        
        item = Item_Fila(str(uuid.uuid4()), tipo, "PENDENTE", dados)
        self.fila.append(item.to_dict())
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

        empresas_service.atualizar_saldo(item["dados"]["destinatario_cnpj"], item["dados"]["valor"])

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
