"""Esse módulo contém a  classe Atacado"""

from produto import Produto

class Atacado:
    """Define o comportamento da classe Atacado"""

    def __init__(self):
        self.__estoque = []
        print ("\ninclusão dos produtos base no estoque\n")

        self.adicionar_produto (Produto(1, "Café 1Kg         ", 53))
        self.adicionar_produto (Produto(2, "Sabão em pó      ", 36))
        self.adicionar_produto (Produto(3, "Caixa de Leite   ", 82))
        self.adicionar_produto (Produto(4, "Refrigerate      ", 8.50))


    def adicionar_produto(self, item:Produto):
        """Adiciona uma instancia de Produto ao estoque do mercado"""
        self.__estoque.append(item)


    def buscar_produto(self, id_produto:int):
        '''Retorna o produto pelo id'''

        for item in self.__estoque:
            if item.get_id() == int(id_produto):
                return item
        return None

    def exibir_estoque(self):
        """Exibe o inventário do estoque do atacado"""

        if len(self.__estoque) == 0:
            print ("\nNão há produtos em estoque!\n")
        else:
            print ("Estoque de produtos do Atacado:\n")

            for item in self.__estoque:
                print(f"ID {item.get_id()} - {item.get_nome()}"
                + f"Valor unitário: {item.get_valor():.2f}")
