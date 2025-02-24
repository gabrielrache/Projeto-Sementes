"""Cria um mercado e seu estoque"""

import json

class Produto:
    """Define o comportamento da classe Produto"""
    def __init__(self, id_produto, nome, quantidade, valor):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor


class Mercado:
    """Define o comportamento da classe Mercado"""
    estoque = []

    @classmethod
    def adiciona_produto(cls, produto: Produto):
        """Adiciona uma instancia de Produto ao estoque do mercado"""
        Mercado.estoque.append(produto)

    @classmethod
    def imprime_estoque(cls):
        """Imprime a lista de produtos e o valor total em estoque"""
        valor_estoque = 0

        for produto in cls.estoque:
            print(f"ID {produto.id_produto} - {produto.nome}. "
                  + f"Quantidade disponível: {produto.quantidade}. "
                  + f"Valor unitário: {produto.valor:.2f}")

            valor_estoque += (produto.valor * produto.quantidade)
        print (f"Valor total em estoque: {valor_estoque:.2f}")

with open("desafio_1/productStock.json", mode="r", encoding="UTF-8") as arquivo:
    produtos_json = json.load(arquivo)

    for item in produtos_json:
        Mercado.adiciona_produto(Produto(item.get("id"),
                                        item.get("nome"),
                                        item.get("quantidade"),
                                        item.get("preco")))

Mercado.imprime_estoque()
