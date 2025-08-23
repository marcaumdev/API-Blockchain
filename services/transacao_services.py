from DTO.transacao import Transacao
from services import Fila_Service

service = Fila_Service()

class Transacao_Service:
    def criar_transacao(self, transacao_data: Transacao):
        # Validações antes de enviar para aprovação
        service.adicionar_na_fila("transacao", transacao_data.model_dump() )
        return {"mensagem": "Transação enviada para aprovação"}
