from pydantic import BaseModel
from datetime import datetime # Valida a data e hora.

class VendaBase(BaseModel):
    total: float
    data_venda_realizada: datetime
    id_vendedor: int
    id_cliente: int

class VendaCreate(VendaBase):
    pass
    
class Venda(VendaBase):
    id: int
    # Este bloco substitui o __init__ e permite que o Pydantic entenda os objetos vindos de bancos de dados ou repositórios.
    class Config:
        from_attributes = True