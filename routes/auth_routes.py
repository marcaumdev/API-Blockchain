from fastapi import APIRouter, HTTPException
from services.empresa_services import Empresa_Service

router = APIRouter(prefix="/auth", tags=["Auth"])
empresas_service = Empresa_Service()

@router.post("/login")
def login(cnpj: int, senha: str):
    usuario = empresas_service.autenticar_empresa(cnpj, senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = empresas_service.criar_token(usuario)
    return {"access_token": token, "token_type": "bearer", "tipo": usuario["tipo"]}