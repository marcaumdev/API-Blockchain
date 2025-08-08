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
