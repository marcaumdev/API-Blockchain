from services.fila_services import Fila_Service

service = Fila_Service()

class Contrato_Service:
    def criar_contrato(self, contrato_data):
        # Aqui você pode validar os dados do contrato antes de adicionar
        service.adicionar_pendente(contrato_data, "contrato")
        return {"mensagem": "Contrato enviado para aprovação"}
