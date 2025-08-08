# blockchain.py
import hashlib
import json
from time import time
from storage import salvar_json, carregar_json

ARQUIVO_BLOCKCHAIN = "blockchain.json"

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



class Blockchain:
    def __init__(self):
        self.cadeia = carregar_json(ARQUIVO_BLOCKCHAIN) or [self.criar_bloco_genesis()]
        self.dificuldade = 2

    def salvar(self):
        salvar_json(ARQUIVO_BLOCKCHAIN, [b if isinstance(b, dict) else b.__dict__ for b in self.cadeia])

    def criar_bloco_genesis(self):
        return Bloco(0, {"mensagem": "Bloco Genesis"}, "0").__dict__

    def obter_ultimo_bloco(self):
        ultimo = self.cadeia[-1]
        if isinstance(ultimo, dict):
            return Bloco(**ultimo)
        return ultimo

    def adicionar_bloco(self, dados):
        ultimo_bloco = self.obter_ultimo_bloco()
        novo_bloco = Bloco(ultimo_bloco.index + 1, dados, ultimo_bloco.hash_atual)
        novo_bloco.prova_de_trabalho(self.dificuldade)
        self.cadeia.append(novo_bloco.__dict__)
        self.salvar()

    def validar_cadeia(self):
        for i in range(1, len(self.cadeia)):
            bloco_atual = Bloco(**self.cadeia[i])
            bloco_anterior = Bloco(**self.cadeia[i-1])
            if bloco_atual.hash_atual != bloco_atual.gerar_hash():
                return False
            if bloco_atual.hash_anterior != bloco_anterior.hash_atual:
                return False
        return True
