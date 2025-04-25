'''Desenha menus e define comportamentos do menu'''

import os
import re

from agenda_telefonica import AgendaTelefonica
from contato import Contato

PAD_FONE = r"^[0-9]{8,9}$"


class Menu:

    @classmethod
    def imprime_menu(cls):
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



    @classmethod
    def ler_opcao(cls):
        '''Lê entrada e retorna opção do menu'''
        try:
            op = int(input())
        except ValueError:
            print("Digite uma opção válida")
            op = cls.ler_opcao()
        return op



    @classmethod
    def ler_contato(cls):
        '''Lê nome e telefone e retorna os dados validados'''

        nome = input("\nDigite o nome do novo contato: ")

        telefone = input("Digite o telefone do contato: ")

        while re.search(PAD_FONE,telefone) is None:
            telefone = input("Digite um telefone válido: ")

        return nome, telefone



    @classmethod
    def opcao_adicionar (cls, agenda:AgendaTelefonica):
        '''Menu auxiliar da opção "Adicionar Contato"'''

        novo_nome, novo_telefone = Menu.ler_contato()
        novo_contato = Contato(novo_nome, novo_telefone)
        agenda.adicionar_contato(novo_contato)



    @classmethod
    def opcao_remover (cls, agenda:AgendaTelefonica):
        '''Menu auxiliar da opção "Remover Contato"'''

        nome = input("\nDigite o nome do contato a ser removido: ")
        agenda.remover_contato(nome)



    @classmethod
    def opcao_buscar (cls, agenda:AgendaTelefonica):
        '''Menu auxiliar da opção "Buscar Contato"'''

        nome = input("\nDigite o nome do contato a ser exibido: ")

        contatos_encontrados = agenda.buscar_contato(nome)

        if len(contatos_encontrados) > 1:
            print (f"foram econtrados {len(contatos_encontrados)} contatos: ")

        elif len(contatos_encontrados) == 1:
            print ("Foi econtrado um contato: ")

        if len(contatos_encontrados) == 0:
            print (f"Contato {nome} não encontrado!")
        else:
            for contato in contatos_encontrados:
                print (f"Nome: {contato.get_nome()}\n" +
                    f"Telefone: {contato.get_telefone()}")



    @classmethod
    def opcao_atualizar (cls, agenda:AgendaTelefonica):
        '''Menu auxiliar da opção "Atualizar Contato'''
        nome = input("\nDigite o nome do contato a ser alterado: ")

        if len(agenda.buscar_contato(nome)) == 0:
            print("Contato não encontrado!")
        else:
            novo_nome = input("\nDigite o novo nome: ")
            novo_telefone = input("Digite o telefone do contato: ")

            while re.search(PAD_FONE,novo_telefone) is None:
                novo_telefone = input("Digite um telefone válido: ")

            agenda.atualizar_contato(nome, Contato(novo_nome, novo_telefone))



    @classmethod
    def opcao_listar (cls, agenda:AgendaTelefonica):
        '''Menu auxiliar da opção "Listar Contatos'''
        os.system('cls')
        agenda.listar_contatos()



    @classmethod
    def executar_operacao(cls, agenda:AgendaTelefonica, op:int):
        '''Executa as operações da agenda telefônica 
            retorna flag para continuar execução'''

        match op:
            case 1:
                cls.opcao_adicionar(agenda)

            case 2:
                cls.opcao_remover(agenda)

            case 3:
                cls.opcao_buscar(agenda)

            case 4:
                cls.opcao_atualizar(agenda)

            case 5:
                cls.opcao_listar(agenda)

            case 0:
                print("Saindo do programa")
                return False

            case _:
                pass

        input("Pressione qualquer tecla para continuar...")
        return True
