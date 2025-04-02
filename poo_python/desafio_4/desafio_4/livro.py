'''Módulo da classe livro'''

class Livro:
    '''Classe auxiliar que define os atributos dos livros da biblioteca'''
    def __init__(self, titulo:str, autor:str):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_titulo(self):
        '''Getter - título do livro'''
        return self.__titulo

    def get_autor(self):
        '''Getter - autor do livro'''
        return self.__autor

    def get_disponivel(self):
        '''Getter - disponibilidade do livro'''
        return self.__disponivel

    def set_disponivel(self, estado:bool):
        '''Setter - disponibilidade do livro'''
        self.__disponivel = estado
