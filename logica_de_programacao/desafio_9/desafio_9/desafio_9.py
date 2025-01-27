"""Lê dois números e realiza a divisão do primeiro pelo segundo"""

while True:
    try:
        dividend = float(input('Digite o dividendo: '))

    except ValueError:
        print('Por favor, digite um número!')

    else:
        break

while True:
    try:
        divisor = float(input('Digite o divisor: '))

    except ValueError:
        print('Por favor, digite um número!')

    else:
        if divisor == 0:
            print('Não é possível realizar divisão por zero!')
        else:
            break


print(f'Quociente: {int(dividend//divisor)}, resto: {int(dividend%divisor)}')
