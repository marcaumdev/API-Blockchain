from fastapi import APIRouter
from models import Blockchain

router = APIRouter(prefix="/blockchain", tags=["Blockchain"])
blockchain = Blockchain()

@router.get("")
def listar_blockchain():
    return blockchain.cadeia

@router.get("/validar")
def validar_blockchain():
    return {"valida": blockchain.validar_cadeia()}
