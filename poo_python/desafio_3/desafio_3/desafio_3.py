'''Classe principal da agenda telefônica'''

from agenda_telefonica import AgendaTelefonica
from menu import Menu


agenda_telefonica = AgendaTelefonica()

continuar = True

while continuar:
    Menu.imprime_menu()

    opcao = Menu.ler_opcao()

    while not 0 <= opcao <= 5:
        print("\nDigite uma opção válida")
        opcao = Menu.ler_opcao()

    continuar = Menu.executar_operacao(agenda_telefonica, opcao)
