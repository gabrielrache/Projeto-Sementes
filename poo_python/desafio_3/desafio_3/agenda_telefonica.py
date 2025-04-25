'''Define atributos e comportamentos da agenda telefônica'''

from contato import Contato

class AgendaTelefonica():
    '''Agenda telefônica que armazena o nome e 
        telefone dos contatos, permitindo operações CRUD com eles'''

    def __init__(self):
        self.__agenda = []

        self.adicionar_contato(Contato("Adriano", "99991111"))
        self.adicionar_contato(Contato("André", "99992222"))
        self.adicionar_contato(Contato("Augusto", "99993333"))
        self.adicionar_contato(Contato("Barbara", "99994444"))
        self.adicionar_contato(Contato("Benhur", "99995555"))
        self.adicionar_contato(Contato("Cleidi", "99996666"))
        self.adicionar_contato(Contato("Eduardo", "99997777"))



    def adicionar_contato(self, novo_contato:Contato):
        '''Adiciona um obj. 'contato' passado por parâmetro à agenda 
            caso ele ainda não exista e retorna se coonseguiu adicionar'''

        for contato in self.__agenda:
            if contato.get_nome() == novo_contato.get_nome():
                print (f"\nO contato {novo_contato.get_nome()} já existe")
                return

        self.__agenda.append(novo_contato)
        print (f"\nContato {novo_contato.get_nome()} criado")



    def remover_contato(self, nome:str):
        '''Remove um obj 'contato' da agenda caso seu 
            nome seja igual ao recebido como parâmetro'''
        removido = False

        for i, contato_armazenado in enumerate(self.__agenda):
            if contato_armazenado.get_nome() == nome:
                del self.__agenda[i]
                removido = True

        if removido:
            print(f"Contato {nome} removido")
        else:
            print(f"{nome} não encontrado!")



    def buscar_contato(self, nome:str) -> list:
        '''Busca um nome na agenda 
            e retorna uma list de obj. 'contato' '''
        contato = []

        for contato_armazenado in self.__agenda:
            if contato_armazenado.get_nome().lower().find(nome.lower()) >= 0:
                contato.append(contato_armazenado)
        return contato



    def atualizar_contato(self, nome:str, novo_contato:Contato):
        '''Atualiza as informações de um obj 'contato'
            substituindo-as pelas novas informações recebidas'''

        # Jeito facil:
        # self.remover_contato(nome)
        # self.adicionar_contato(novo_contato)

        # Implementação de um update real:
        for contato in self.__agenda:
            if contato.get_nome().lower() == novo_contato.get_nome().lower():
                print (f"\nO contato {novo_contato.get_nome()} já existe")
                return

        for i, contato_armazenado in enumerate(self.__agenda):
            if contato_armazenado.get_nome().lower() == nome.lower():
                self.__agenda[i].set_nome(novo_contato.get_nome())
                self.__agenda[i].set_telefone(novo_contato.get_telefone())
                print (f"\nContato {nome} atualizado para {novo_contato.get_nome()}")



    def listar_contatos(self):
        '''Lista todos os contatos na agenda'''
        if len(self.__agenda) == 0:
            print("Nenhum contato a exibir\n")

        for i, contato_armazenado in enumerate(self.__agenda):
            print (f"{i+1} - Nome: {contato_armazenado.get_nome()}\n" +
                   f"   Telefone: {contato_armazenado.get_telefone()}")
