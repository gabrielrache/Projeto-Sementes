"""Autentica um usuário e senha, bloqueando o sistema caso inserido com erro repetidas vezes"""

authenticated = False

for count in range (3):

    while True:
        user = input("Digite seu usuário: ")

        if len(user) > 0:
            break

    while True:
        password = input("Digite a sua senha: ")

        if len(password) > 0:
            break


    if user == 'aluno' and password == 'segredo':
        print("bem-vindo!")
        authenticated = True
        break

    print('Usuário ou senha incorretos')

if not authenticated:
    print("Excedeu limite de tentativas - Login bloqueado!")
