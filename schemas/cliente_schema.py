from datetime import datetime
from ..schemas.pessoa_schema import PessoaBase # Contém os dados comuns.
# O arquivo pessoa_schema.py é automaticamente "copiado" para o ClienteCreate e para o Cliente.

class ClienteCreate(PessoaBase):
    pass

class Cliente(PessoaBase):
    id: int
    id_pessoa: int
    data_cadastro: datetime
    
    class Config: # Essencial para o FastAPI e Pydantic.
       from_attributes: True