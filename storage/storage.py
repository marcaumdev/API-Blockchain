# storage.py
import json
import os

def salvar_json(nome_arquivo, dados):
    with open(nome_arquivo, "w") as f:
        json.dump(dados, f, indent=4)

def carregar_json(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r") as f:
        return json.load(f)

def excluir_registro(nome_arquivo, campo, valor):
    """
    Exclui um registro do arquivo JSON pelo campo escolhido.
    Retorna True se foi excluído, False se não encontrou.
    """
    dados = carregar_json(nome_arquivo)
    tamanho_inicial = len(dados)

    # Mantém apenas os itens cujo id é diferente do informado
    dados = [item for item in dados if str(item.get(campo)) != str(valor)]

    if len(dados) == tamanho_inicial:
        return False  # Nenhum item foi removido

    salvar_json(nome_arquivo, dados)
    return True
