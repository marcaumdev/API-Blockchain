from fastapi import APIRouter, HTTPException
from services import Empresa_Service
from models import Blockchain
from DTO import Transacao

router = APIRouter(prefix="/transacao", tags=["Transações"])
empresas_service = Empresa_Service()
blockchain = Blockchain()

@router.post("")
def criar_transacao(dados: Transacao):
    remetente = empresas_service.buscar_por_id(dados.remetente_id)
    destinatario = empresas_service.buscar_por_id(dados.destinatario_id)
    
    if not remetente or not destinatario:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    if remetente["saldo"] < dados.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    empresas_service.atualizar_saldo(dados.remetente_id, -dados.valor)
    empresas_service.atualizar_saldo(dados.destinatario_id, dados.valor)

    blockchain.adicionar_bloco({
        "tipo": "transacao",
        "remetente": remetente["nome"],
        "destinatario": destinatario["nome"],
        "valor": dados.valor
    })
    return {"mensagem": "Transação registrada com sucesso"}
