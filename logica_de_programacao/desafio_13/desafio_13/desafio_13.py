"""Busca um nome no vetor de nomes informado"""


def read_name():
    """Lê um nome válido"""

    name = ''

    while len(name) == 0:
        name = input("Digite um nome: ")

        if len(name) == 0:
            print ("Por favor, digite um nome válido!")

    return name

name_list = []


for count in range(10):

    print(f"inclusão de nomes - Iteração {count+1}")
    name_list.append(read_name())

print("Etapa de busca")
searched_name = read_name()

if  searched_name in name_list:
    print("Achei")
else:
    print("Não achei")
