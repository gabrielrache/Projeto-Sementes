'''Módulo auxiliar para impressão dos menus no terminal'''

import os

def imprimir_menu_principal():
    '''Escreve a interface do menu principal no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n\n\n"
        "Menu: \n\n"
        "1 - Adicionar livro ao acervo\n"
        "2 - Ferramenta de busca\n"
        "3 - Pegar livro emprestado\n"
        "4 - Devolver livro\n"
        "0 - Sair\n")


def imprimir_menu_busca():
    '''Escreve a interface do menu "buscar" no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n"
        "> Ferramenta de busca\n\n"
        "Menu: \n\n"
        "1 - Busca por título\n"
        "2 - Busca por autor\n"
        "3 - Listar tudo\n"
        "0 - Voltar\n")

def imprimir_menu_busca_listar(submenu:int):
    '''Escreve a interface do submenus de buscar no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n"
        "> Ferramenta de busca")
    match submenu:
        case 1:
            print(">> Busca por Título\n")
        case 2:
            print(">> Busca por Autor\n")
        case 3:
            print(">> Busca completa\n")


def imprimir_menu_inclusao():
    '''Escreve a interface do menu de inclusão no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n"
        "> Adicionar livro ao acervo\n\n")


def imprimir_menu_emprestar():
    '''Escreve a interface do menu emprestar no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n"
          "> Pegar livro emprestado\n\n"
          "Selecione um livro do acervo para empréstimo:")

def imprimir_menu_devolver():
    '''Escreve a interface do menu emprestar no terminal'''
    os.system('cls')
    print("Sistema de Biblioteca\n"
          "> Devolver livro\n\n"
          "Selecione um livro do acervo para devolução:")
