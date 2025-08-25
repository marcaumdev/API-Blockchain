from pydantic import BaseModel

class Item_Fila(BaseModel):
    id: str
    tipo: str
    dados: dict
    status: str