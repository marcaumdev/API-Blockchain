import hashlib
import json
from time import time

class Bloco:
    def __init__(self, index, dados, hash_anterior='', timestamp=None, nonce=0, hash_atual=None):
        self.index = index
        self.timestamp = timestamp or time()
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.nonce = nonce
        self.hash_atual = hash_atual or self.gerar_hash()

    def gerar_hash(self):
        conteudo = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "dados": self.dados,
            "hash_anterior": self.hash_anterior,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(conteudo).hexdigest()

    def prova_de_trabalho(self, dificuldade):
        while self.hash_atual[:dificuldade] != '0' * dificuldade:
            self.nonce += 1
            self.hash_atual = self.gerar_hash()
