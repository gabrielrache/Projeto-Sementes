"""Esse módulo contém a  classe Atacado"""
from produto import Produto

class Atacado:
    """Define o comportamento da classe Atacado"""
    _estoque = []

    @classmethod
    def adicionar_produto(cls, item: Produto):
        """Adiciona uma instancia de Produto ao estoque do mercado"""
        Atacado._estoque.append(item)

    @classmethod
    def buscar_produto(cls, id):
        
        for item in cls._estoque:
            if item.get_id() == int(id):
                return item
        return None    

    @classmethod
    def exibir_estoque(cls):
        """Exibe o inventário do estoque do atacado"""

        if len(cls._estoque) == 0:
            print ("Não há produtos em estoque!\n")
        else:
            print ("Estoque de produtos do Atacado:\n")

            for item in cls._estoque:
                print(f"ID {item._id_produto} - {item._nome}. "
                + f"Valor unitário: {item._valor:.2f}")
