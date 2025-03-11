"""Esse módulo contém a classe CaixaDoAtacado"""

import csv
import os
from atacado import Atacado

class CaixaDoAtacado():
    """Define o comportamento dos caixas do Atacado"""

    def __init__(self, numero_caixa):
        self._numero = numero_caixa
        print (f"Caixa {self._numero} aberto")

    def get_numero(self):
        '''Getter numero'''
        return self._numero

    @classmethod
    def listar_pedidos(cls):
        '''Lista todos os pedidos disponíveis para computar no diretório'''
        pedidos_path = "desafio_2/pedidos"

        pedidos = os.listdir(pedidos_path)

        if len(pedidos) == 0:
            print ("Não foram encontrados pedidos a processar")

        for i in pedidos:
            print(i)

    @classmethod
    def _ler_arquivo (cls, numero):

        path_arq = "desafio_2/pedidos/" + str(numero) + ".csv"

        try:
            with open(path_arq, "r", encoding="utf-8") as arquivo:

                pedido_csv = csv.reader(arquivo, delimiter=",")
                pedido = []

                for linha in pedido_csv:
                    pedido.append(linha)

        except FileNotFoundError:
            print("O pedido informado não foi encontrado.")

        except IOError:
            print("Ocorreu um erro ao tentar ler o pedido.")

        except Exception as e:
            print(f"Um erro inesperado ocorreu: {e}")

        return pedido


    def computar_compra (self,numero):
        """Método que computa o valor da compra e seus descontos"""

        pedido = self._ler_arquivo(numero)
        valor_compra = 0
        cupom_fiscal = []

        if len(pedido) > 1:

            for i, registro in enumerate(pedido):

                if i == 0:
                    if str(registro[0]) in ('debito', 'credito', 'dinheiro'):
                        pagamento = str(registro[0])
                    else:
                        pagamento = "não informado"

                    cupom_fiscal.append("\n------------------------------------")
                    cupom_fiscal.append("------------CUPOM FISCAL------------")
                    cupom_fiscal.append("------------------------------------")
                else:
                    id_produto = int(registro[0])
                    quantidade = int(registro[1])
                    desconto = 0

                    produto = Atacado.buscar_produto(id_produto)

                    if produto is not None:

                        if quantidade > 25:
                            valor = produto.get_valor() * 0.75
                            desconto = 25
                        elif quantidade >= 15:
                            valor = produto.get_valor() * 0.80
                            desconto = 20
                        elif quantidade >= 5:
                            valor = produto.get_valor() * 0.90
                            desconto = 10
                        else:
                            valor = produto.get_valor()

                        valor_compra = valor * quantidade

                        cupom_fiscal.append(f"{i} - {produto.get_nome()} {quantidade}x {valor:.2f}")
                        cupom_fiscal.append(f"Desconto aplicado: " +
                                            f"{desconto}% = {valor_compra:.2f}\n")

            cupom_fiscal.append(f"\nForma de pagamento selecionada: {pagamento}")

            match pagamento.lower():

                case 'dinheiro':
                    valor_compra *= 0.95
                    cupom_fiscal.append("Desconto de 5% aplicado para essa forma de pagamento")

                case 'credito':
                    valor_compra *= 1.03
                    cupom_fiscal.append("Acréscimo de 3% aplicado para essa forma de pagamento")

                case _:
                    cupom_fiscal.append("Não há desconto para essa forma de pagamento")


            cupom_fiscal.append(f"\nTotal do pedido: {valor_compra}")

            for i in cupom_fiscal:
                print (i)
