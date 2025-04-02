'''Módulo da classe biblioteca'''

import sys
from livro import Livro

class Biblioteca:
    '''Classe responsável pela manutenção do acervo da biblioteca'''
    __acervo = []

###############################################################################################

###########################
## ROTINAS DE MANUTENÇÃO ##
###########################

    @classmethod
    def inicializar_acervo(cls):
        '''Adiciona objetos Livro pré-definidos ao acervo inicial da biblioteca'''
        print(cls.adicionar_livro(Livro("1984", "George Orwell")))
        print(cls.adicionar_livro(Livro("Cosmos", "Karl Sagan")))
        print(cls.adicionar_livro(Livro("Eu, Robô", "Isac Asimov")))
        print(cls.adicionar_livro(Livro("Silmarillion, O", "J. R. R. Tolkien")))
        print(cls.adicionar_livro(Livro("Torre Negra, A", "Stephen King")))
        print(cls.adicionar_livro(Livro("Universo numa Casca de Noz, O", "Stephen Hawking")))
        print(cls.adicionar_livro(Livro("Viagens de Gulliver, As", "Jonathan Swift")))

    @classmethod
    def criar_livro(cls):
        '''Solicita input de título e de autor, retornando um objeto Livro'''
        try:
            titulo = ''
            while len(titulo) == 0:
                titulo = input("Digite o título do novo livro: ")
                if len(titulo) == 0:
                    print("Erro - Digite um título válido!")

            autor = ''
            while len(autor) == 0:
                autor = input("Digite o nome do autor: ")
                if len(autor) == 0:
                    print("Erro - Digite um autor válido!")

        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário!")
            sys.exit(0)

        return Livro(titulo,autor)

    @classmethod
    def adicionar_livro(cls,novo_livro:Livro):
        '''Adiciona um objeto Livro ao acervo da biblioteca.
            Retorna uma mensagem de status da executação'''
        for livro in cls.__acervo:
            try:
                if (livro.get_titulo().lower() == novo_livro.get_titulo().lower()
                and livro.get_autor().lower() == novo_livro.get_autor().lower()):
                    raise Exception

            except Exception:

                return (f"\nErro - O livro '{novo_livro.get_titulo()}' "
            f"de {novo_livro.get_autor()} já consta no acervo da biblioteca"
            " e não pode ser adicionado novamente.\n")

        cls.__acervo.append(novo_livro)
        return (f"\nO livro '{novo_livro.get_titulo()}' "
            f"de {novo_livro.get_autor()} adicionado ao acervo.\n")

###############################################################################################

######################
## ROTINAS DE BUSCA ##
######################

    @classmethod
    def localizar_livros(cls, operacao:int):
        '''Localiza livros no acervo conforme operação recebida no parâmetro
        e retorna a lista de livros que atendem ao critério de busca'''
        livros = []

        match operacao:
            case 1:
                # busca por título
                titulo = ''
                while len(titulo) == 0:
                    titulo = input("Digite o título a ser pesquisado: ")
                livros = cls.localizar_por_titulo(titulo)

            case 2:
                # busca por autor
                autor = ''
                while len(autor) == 0:
                    autor = input("Digite o autor a ser pesquisado: ")
                livros = cls.localizar_por_autor(autor)

            case 3:
                # busca sem filtro
                livros = cls.localizar_tudo()
        return livros




    @classmethod
    def localizar_por_titulo(cls, titulo:str):
        '''Localiza livros pelo título no acervo da biblioteca 
        e retorna uma lista com os objetos Livro'''
        livros = []
        for livro_armazenado in cls.__acervo:
            if titulo.lower() in livro_armazenado.get_titulo().lower():
                livros.append(livro_armazenado)
        return livros

    @classmethod
    def localizar_por_autor(cls, autor:str):
        '''Localiza livros pelo autor no acervo da biblioteca 
        e retorna uma lista com os objetos Livro'''
        livros = []
        for livro_armazenado in cls.__acervo:
            if autor.lower() in livro_armazenado.get_autor().lower():
                livros.append(livro_armazenado)
        return livros

    @classmethod
    def localizar_tudo(cls):
        '''Retorna a lista completa de livros do acervo'''
        return cls.__acervo

    @classmethod
    def imprimir_busca(cls, livros:list):
        '''imprime a lista de livros passada por parâmetro'''
        print("")
        for i, livro in enumerate(livros):
            disponibilidade = "disponível" if livro.get_disponivel() else "Indisponível"
            print (f"{i+1} - {livro.get_titulo()} - {livro.get_autor()} - {disponibilidade}")
        print("")



###############################################################################################

###########################
## ROTINAS DE EMPRÉSTIMO ##
###########################

    @classmethod
    def escolher_livro(cls, livros:list):
        '''imprime a lista de livros passada no parâmetro e retorna apenas um livro'''

        livro = []

        match len(livros):
            case 0:
                print("Nenhum livro encontrado! Mostrando acervo completo.")
                livros = cls.__acervo

            case 1:
                livro = livros[0]

            case _:
                for i, livro in enumerate(livros):
                    disponibilidade = "disponível" if livro.get_disponivel() else "Indisponível"
                    print(f"{i+1} - {livro.get_titulo()} - {livro.get_autor()} - {disponibilidade}")

                repetir = True

                while repetir:

                    try:
                        id_livro = int(input("Digite o número do livro desejado: "))
                    except ValueError:
                        print("Erro - Opção inválida! Tente novamente.")
                        continue
                    except KeyboardInterrupt:
                        print("\nOperação cancelada pelo usuário!")
                        sys.exit(0)


                    try:
                        if id_livro > 0:
                            livro = livros[id_livro-1]
                            repetir = False
                        raise IndexError
                    except IndexError:
                        print("Erro - Opção inválida! Tente novamente.")

        return livro

    @classmethod
    def emprestar_livro(cls, livro:Livro):
        '''Tenta emprestar um livro do acervo da biblioteca'''
        try:
            if livro.get_disponivel():
                livro.set_disponivel(False)
                print(f"\nLivro '{livro.get_titulo()}' emprestado com sucesso!")
            else:
                raise Exception

        except Exception:
            print(f"\nErro - O livro '{livro.get_titulo()}' não está disponível para empréstimo!")



    @classmethod
    def devolver_livro(cls, livro:Livro):
        '''Tenta devolver um livro emprestado ao acervo da biblioteca'''
        try:
            if not livro.get_disponivel():
                livro.set_disponivel(True)
                print(f"\nLivro '{livro.get_titulo()}' devolvido com sucesso!")
            else:
                raise Exception

        except Exception:
            print(f"\nErro - O livro '{livro.get_titulo()}' não foi emprestado!")
