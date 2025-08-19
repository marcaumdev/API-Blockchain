from services import Fila_Service

service = Fila_Service()

class Transacao_Service:
    def criar_transacao(self, transacao_data):
        # Validações antes de enviar para aprovação
        service.adicionar_pendente(transacao_data, "transacao")
        return {"mensagem": "Transação enviada para aprovação"}
