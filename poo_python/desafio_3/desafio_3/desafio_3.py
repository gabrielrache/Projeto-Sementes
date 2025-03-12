'''Classe principal da agenda telefônica'''

import os
import re

from contato import Contato
from agenda_telefonica import AgendaTelefonica

def ler_opcao():
    '''Lê entrada e retorna opção do menu'''
    try:
        op = int(input())
    except ValueError:
        print("Digite uma opção válida")
        op = ler_opcao()
    return op


def imprime_menu():
    '''Imprime o menu principal do programa no console'''

    os.system('cls')
    print(
"""AGENDA TELEFÔNICA

   ▄▄██████▄▄
 ▄██▀▄█▄▄█▄▀██▄
 ▀▀▀▄██▀▀██▄▀▀▀
  ▄███─██─███▄
  █████▄▄█████

MENU:
1 - ADICIONAR CONTATO
2 - REMOVER CONTATO
3 - BUSCAR CONTATO
4 - ATUALIZAR CONTATO
5 - LISTAR CONTATOS

0 - SAIR

DIGITE A OPÇÃO DESEJADA: """)


def executar_operacao(op):
    '''Executa as operações da agenda telefônica 
        retorna flag para continuar execução'''

    match op:
        case 1:
            nome = input("\nDigite o nome do novo contato: ")
            telefone = input("Digite o telefone do contato: ")

            while re.search(PAD_FONE,telefone) is None:
                telefone = input("Digite um telefone válido: ")

            AgendaTelefonica.adicionar_contato(Contato(nome, telefone))

            input("Pressione qualquer tecla para continuar...")
            return True

        case 2:
            nome = input("\nDigite o nome do contato a ser removido: ")

            AgendaTelefonica.remover_contato(nome)

            input("Pressione qualquer tecla para continuar...")
            return True


        case 3:
            nome = input("\nDigite o nome do contato a ser exibido: ")

            contato = AgendaTelefonica.buscar_contato(nome)

            print (f"Nome: {contato.get_nome()}\n" +
                   f"Telefone: {contato.get_telefone()}")

            input("Pressione qualquer tecla para continuar...")
            return True

        case 4:
            nome = input("\nDigite o nome do contato a ser alterado: ")
            if AgendaTelefonica.buscar_contato(nome) is None:
                print("Contato não encontrado!")
            else:
                novo_nome = input("\nDigite o novo nome: ")
                telefone = input("Digite o telefone do contato: ")

                while re.search(PAD_FONE,telefone) is None:
                    telefone = input("Digite um telefone válido: ")

                AgendaTelefonica.atualizar_contato(nome, Contato(novo_nome, telefone))
            input("Pressione qualquer tecla para continuar...")
            return True

        case 5:
            os.system('cls')
            AgendaTelefonica.listar_contatos()

            input("Pressione qualquer tecla para continuar...")
            return True

        case 0:
            print("Saindo do programa")
            input("Pressione qualquer tecla para continuar...")
            return False

        case _:
            return True

#########

PAD_FONE = r"^[0-9]{8,9}$"

continuar = True

while continuar:
    print("Comecei")
    imprime_menu()
    opcao = ler_opcao()

    while not 0 <= opcao <= 5:
        print("\nDigite uma opção válida")
        opcao = ler_opcao()

    continuar = executar_operacao(opcao)
