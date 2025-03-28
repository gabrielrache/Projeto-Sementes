'''Define atributos e comportamentos da agenda telefônica'''
import re

from contato import Contato

PAD_FONE = r"^[0-9]{8,9}$"

class AgendaTelefonica:
    '''Define a Classe AgendaTelefonica'''
    __agenda = []

    @classmethod
    def buscar_contato(cls, nome:str):
        '''Busca um nome na agenda 
            e retorna um obj. 'contato' '''
        contato = []

        for contato_armazenado in cls.__agenda:
            if contato_armazenado.get_nome().lower().find(nome.lower()) >= 0:
                contato.append(contato_armazenado)

        return contato


    @classmethod
    def adicionar_contato(cls):
        '''Adiciona um obj. 'contato' à agenda 
            caso ele ainda não exista'''

        nome = input("\nDigite o nome do novo contato: ")

        for contato in cls.__agenda:
            if contato.get_nome() == nome:
                print (f"\nO contato {nome} já existe")
                return

        telefone = input("Digite o telefone do contato: ")

        while re.search(PAD_FONE,telefone) is None:
            telefone = input("Digite um telefone válido: ")

        cls.__agenda.append(Contato(nome,telefone))
        print (f"\nContato {nome} criado")


    @classmethod
    def remover_contato(cls, nome:str):
        '''Remove um obj 'contato' da agenda 
            caso tenha o nome igual ao recebido'''
        removido = False

        for i, contato_armazenado in enumerate(cls.__agenda):
            if contato_armazenado.get_nome() == nome:
                del cls.__agenda[i]
                removido = True

        if removido:
            print(f"Contato {nome} removido")
        else:
            print(f"{nome} não encontrado!")

    @classmethod
    def atualizar_contato(cls, nome:str, novo_contato:Contato):
        '''Atualiza as informações de um obj 'contato'
            substituindo-as pelas novas informações recebidas'''

        # Jeito facil:
        # cls.remover_contato(nome)
        # cls.adicionar_contato(novo_contato)

        # Implementação de um update real:
        for i, contato_armazenado in enumerate(cls.__agenda):
            if contato_armazenado.get_nome() == nome:
                cls.__agenda[i].set_nome(novo_contato.get_nome())
                cls.__agenda[i].set_telefone(novo_contato.get_telefone())
                print (f"\nContato {nome} atualizado para {novo_contato.get_nome()}")


    @classmethod
    def listar_contatos(cls):
        '''Lista todos os contatos na agenda'''
        if len(cls.__agenda) == 0:
            print("Nenhum contato a exibir\n")

        for i, contato_armazenado in enumerate(cls.__agenda):
            print (f"{i+1} - Nome: {contato_armazenado.get_nome()}\n" +
                   f"   Telefone: {contato_armazenado.get_telefone()}")
