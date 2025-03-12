'''Define atributos e comportamentos da agenda telefônica'''

class AgendaTelefonica:
    '''Define a Classe AgendaTelefonica'''
    __agenda = []

    @classmethod
    def buscar_contato(cls, nome):
        '''Busca um nome na agenda 
            e retorna um obj. 'contato' '''
        for contato_armazenado in cls.__agenda:
            if contato_armazenado.get_nome().lower() == nome.lower():
                return contato_armazenado
        return None

    @classmethod
    def adicionar_contato(cls, novo_contato):
        '''Adiciona um obj. 'contato' à agenda 
            caso ele ainda não exista'''
        if cls.buscar_contato(novo_contato.get_nome()) is None:
            cls.__agenda.append(novo_contato)
            print (f"\nContato {novo_contato.get_nome()} criado")
        else:
            print (f"\nO contato {novo_contato.get_nome()} já existe")

    @classmethod
    def remover_contato(cls, nome):
        '''Remove um obj 'contato' da agenda 
            caso tenha o nome igual ao recebido'''
        if cls.buscar_contato(nome) is None:
            print(f"Contato {nome} não localizado")
        else:
            for i, contato_armazenado in enumerate(cls.__agenda):
                if contato_armazenado == cls.buscar_contato(nome):
                    del cls.__agenda[i]
                    print(f"Contato {nome} removido")

    @classmethod
    def atualizar_contato(cls, nome, novo_contato):
        '''Atualiza as informações de um obj 'contato'
            substituindo-as pelas novas informações recebidas'''

        # Jeito facil:
        # cls.remover_contato(nome)
        # cls.adicionar_contato(novo_contato)

        # Implementação de um update real:
        for i, contato_armazenado in enumerate(cls.__agenda):
            if contato_armazenado == cls.buscar_contato(nome):
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
