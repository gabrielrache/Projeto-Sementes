'''Define atributos e comportamentos dos contatos da agenda telefônica'''

class Contato:
    '''Define a Classe Contato'''
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone


    def get_nome(self):
        '''Getter Contato.nome'''
        return self.__nome

    def get_telefone(self):
        '''Getter Contato.telefone'''
        return self.__telefone

    def set_nome(self,novo_nome):
        '''Setter Contato.nome'''
        self.__nome = novo_nome

    def set_telefone(self,novo_telefone):
        '''Setter Contato.telefone'''
        self.__telefone = novo_telefone
