from schemas.item_venda_schema import ItemVenda

items_vendas = []

class ItemVendaRepository: # Liga um Produto específico a uma Venda realizada.

    def cadastrar_item_venda(self, id_produto, quantidade, id_venda):
        item_venda = ItemVenda(1, id_produto, quantidade, id_venda)
        items_vendas.append(item_venda)
        return item_venda