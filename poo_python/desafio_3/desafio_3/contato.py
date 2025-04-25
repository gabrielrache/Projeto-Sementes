'''Define atributos e comportamentos dos contatos da agenda telefônica'''

class Contato:
    '''Define a Classe Contato'''
    def __init__(self, nome:str, telefone:str):
        self.__nome = nome
        self.__telefone = telefone


    def get_nome(self) -> str:
        '''Getter Contato.nome'''
        return self.__nome

    def get_telefone(self) -> str:
        '''Getter Contato.telefone'''
        return self.__telefone

    def set_nome(self,novo_nome:str):
        '''Setter Contato.nome'''
        self.__nome = novo_nome

    def set_telefone(self,novo_telefone:str):
        '''Setter Contato.telefone'''
        self.__telefone = novo_telefone
