"""Gera um vetor de números aleatórios"""

value_list = []
count = 0

for x in range (1,11):

    try:
        value_list.append (int(input(f"Digite o valor {x}: ")))

    except ValueError:
        continue


for value in value_list:
    if value%2 > 0:
        count += 1

print(f"Foram digitados {count} valores impares")
