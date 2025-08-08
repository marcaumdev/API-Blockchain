# main.py
from fastapi import FastAPI, HTTPException
from empresa import EmpresaService
from blockchain import Blockchain
from models import EmpresaInput, TransacaoInput, ContratoInput

app = FastAPI(title="Blockchain Empresas API")

empresas_service = EmpresaService()
blockchain = Blockchain()

@app.post("/empresa")
def criar_empresa(dados: EmpresaInput):
    empresa = empresas_service.criar_empresa(dados.nome, dados.saldo_inicial)
    return empresa

@app.get("/empresa")
def listar_empresas():
    return empresas_service.listar()

@app.post("/transacao")
def criar_transacao(dados: TransacaoInput):
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

@app.post("/contrato")
def criar_contrato(dados: ContratoInput):
    empresa = empresas_service.buscar_por_id(dados.empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")

    blockchain.adicionar_bloco({
        "tipo": "contrato",
        "empresa": empresa["nome"],
        "descricao": dados.descricao,
        "valor": dados.valor
    })
    return {"mensagem": "Contrato registrado com sucesso"}

@app.get("/blockchain")
def listar_blockchain():
    return blockchain.cadeia

@app.get("/validar")
def validar_blockchain():
    return {"valida": blockchain.validar_cadeia()}
