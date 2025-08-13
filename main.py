from fastapi import FastAPI
from routes import empresa_routes, transacao_routes, contrato_routes, blockchain_routes

app = FastAPI(title="Din API")

# Registrando rotas
app.include_router(empresa_routes.router)
app.include_router(transacao_routes.router)
app.include_router(contrato_routes.router)
app.include_router(blockchain_routes.router)
