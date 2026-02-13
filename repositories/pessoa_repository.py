from ..schemas.pessoa_schema import PessoaCreate, Pessoa
# Importa as "regras" de como uma Pessoa deve ser estruturada.

pessoas = []

class PessoaRepository: # Agrupa as ações com os dados de uma Pessoa
    """Insere um registro da Pessoa no banco de dados."""
    def cadastrar_pessoa(self, pessoa_data: PessoaCreate):
       novo_id = len(pessoas) + 1
       
       pessoa = Pessoa(
           id = novo_id,
           **pessoa_data.model_dump()
       )

       pessoas.append(pessoa)
       return pessoa 
    
    def buscar_pessoa(self, id_pessoa):
        """Realiza a busca de uma Pessoa no banco de Dados passando seu ID."""
        for pessoa in pessoas:
            if(pessoa.id == id_pessoa):
                return pessoa