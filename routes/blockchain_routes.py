from fastapi import APIRouter
from fastapi.params import Depends
from models import Blockchain
from services import autenticacao

router = APIRouter(prefix="/blockchain", tags=["Blockchain"])
blockchain = Blockchain()

@router.get("")
def listar_blockchain():
    return blockchain.cadeia

@router.get("/validar", dependencies=[Depends(autenticacao)])
def validar_blockchain():
    return {"valida": blockchain.validar_cadeia()}
