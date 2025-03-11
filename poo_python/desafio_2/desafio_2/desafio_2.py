"""Módulo principal do programa"""
from produto import Produto
from atacado import Atacado
from caixa_do_atacado import CaixaDoAtacado

print ("\nDefinição dos produtos\n")

cafe = Produto(1, "Café 1Kg", 53)
sabao = Produto(2, "Sabão em pó", 36)
leite = Produto(3, "Caixa de Leite", 82)
refri = Produto(4, "Refrigerate", 8.50)


print ("\ninclusão dos produtos no estoque\n")


Atacado.adicionar_produto(cafe)
Atacado.adicionar_produto(sabao)
Atacado.adicionar_produto(leite)
Atacado.adicionar_produto(refri)


print ("\nAbertura dos caixas")

caixa1 = CaixaDoAtacado(1)
caixa2 = CaixaDoAtacado(2)


print ("\nPedidos pendentes de processamento: \n")

CaixaDoAtacado.listar_pedidos()


caixa1.computar_compra(101030)
