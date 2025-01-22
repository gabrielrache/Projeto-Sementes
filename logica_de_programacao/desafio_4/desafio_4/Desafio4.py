import os

def montaTela (a, operator, b, result):
    os.system("cls")
    print ('-----------------------')
    print ('Desafio 4 - Calculadora')
    print ('-----------------------\n')

    if result is not None:
        print (f'{a} {operator} {b} = {result}')

    elif b is not None:
        print (f'{a} {operator} {b}')

    elif operator is not None:
            print (f'{a} {operator}')
    elif a is not None:
        print (f'{a}')


while True:
    montaTela(None,None,None,None)
    a = float(input('\ndigite o primeiro termo: '))

    montaTela(a,None,None,None)
    operator = input('digite o operador matemático: ')

    montaTela(a,operator,None,None)
    b = float(input('digite o segundo termo: '))

    solution = None

    match operator:
        case 'x'|'X'|'*':
            solution = a*b

        case '/' | ':':
            solution = a/b

        case '+':
            solution = a+b
        case '-':
            solution = a-b
        case _:
            print ('operador não encontrado')

    if solution is not None:
        montaTela(a,operator,b,solution)

    repeat = 0

    while repeat != 'y' and repeat != 'n':
        montaTela(a,operator,b,solution)
        repeat = input('Continuar? (y/n)')

    if repeat == 'n':
        break