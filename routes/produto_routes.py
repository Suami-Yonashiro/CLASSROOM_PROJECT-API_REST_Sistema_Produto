from fastapi import HTTPException, APIRouter, status # Tratamento de Erros.
from ..services.produto_service import produto_service
from ..schemas.produto_schema import Produto, ProdutoCreate

router = APIRouter(
    prefix="/produto",
    tags=["Produto"]
)

@router.post(
    "/",
    response_model=Produto,
    status_code=status.HTTP_201_CREATED # Sucesso de criar.
)
def registrar_produto(produto_data: ProdutoCreate) -> Produto:
    produto = produto_service.cadastrar_produto(produto_data) # Roteador delega a tarefa para o serviço.
    return produto

@router.get(
    "/{id_produto}",
    response_model=Produto,
    status_code=200 # Sucesso ao ler.
)
def buscar_produto(id_produto: int) -> Produto:
    produto = produto_service.buscar_produto(id_produto)
    if not produto: # Verifica se o serviço retornou algo.
        raise HTTPException( # Interrompe a execução e envia uma resposta imediata para o usuário.
            status_code=404, # Erro porque o dado não existe.
            detail="Produto não Encontrado"
        )
    return produto