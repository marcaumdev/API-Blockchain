from fastapi import APIRouter, HTTPException
from services.empresa_services import Empresa_Service
from DTO import Login

router = APIRouter(prefix="/auth", tags=["Auth"])
empresas_service = Empresa_Service()

@router.post("/login")
def login(login_data: Login):
    usuario = empresas_service.autenticar_empresa(login_data)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = empresas_service.criar_token(usuario)
    return {"access_token": token, "token_type": "bearer", "tipo": usuario["tipo"]}