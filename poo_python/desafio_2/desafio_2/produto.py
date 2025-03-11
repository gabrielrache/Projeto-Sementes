"""Esse módulo contém a classe Produto"""

class Produto:
    """Define os produtos a serem estocados e vendidos pelo Atacado"""

    def __init__(self, id_produto, nome, valor):
        self._id_produto = int(id_produto)
        self._nome = str(nome)
        self._valor = float(valor)

        print (f"{nome} adicionado ao estoque!")

    def get_id(self):
        '''Getter _id_produto'''
        return self._id_produto

    def get_nome(self):
        '''Getter _nome'''
        return self._nome

    def get_valor(self):
        '''Getter _valor'''
        return self._valor
