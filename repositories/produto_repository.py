from ..schemas.produto_schema import Produto, ProdutoCreate # Contém o que é necessário para criar o Produto.

produtos = []

class ProdutoRepository:
    """Efetua o Registro de um novo produto no banco de dados."""
    def cadastrar_produto(self, produto_data: ProdutoCreate):
       produto = Produto(
           id = len(produtos) + 1,
           **produto_data.model_dump()
        )
       
       produtos.append(produto)
       return produto 
    
    
    def buscar_produto(self, produto_id):
        """Efetua a Busca de um produto no banco de Dados passando seu ID."""
        for produto in produtos: # O código entra na lista e olha Produto por Produto.
            if(produto.id == produto_id):
                return produto

produto_repository = ProdutoRepository()