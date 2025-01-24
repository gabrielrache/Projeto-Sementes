"""Calcula a média de notas e retorna aa situação"""
print ('--------------------------------')
print ('Desafio 3 - Calculadora de notas')
print ('---------------------------------\n\n')


grade = []

for i in range(1,4):
    grade.append (float(input(f'Digite a nota {i}: ')))


average = sum(grade) / len(grade)

print(f'\nMédia alcançada:\n {average}\nConceito:')
if average >= 7:
    print('Aprovado\n')
elif average >= 5:
    print('Recuperação\n')
else:
    print('Reprovado\n')
