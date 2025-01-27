"""Lê um número inteiro entre 1 e 10 e escreve a sua tabuada"""

number = 0

while number < 1 or number > 10:
    try:
        number = int(input('Digite um número inteiro entre 1 e 10: '))

    except ValueError:
        number = 0

    finally:
        if number < 1 or number > 10:
            print('Digite um número válido para continuar')


print (f'Tabuada do {number}: ')


for numerator in range (1,11):
    print (f'{numerator} x {number} = {numerator*number}')
