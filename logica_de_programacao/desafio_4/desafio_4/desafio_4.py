"""Implementação simples de uma calculadora de quatro operações"""
import os

def monta_tela (a_value, operator_str, b_value, result):
    """IMprime a UI da calculadora no terminal"""
    os.system("cls")
    print ('-----------------------')
    print ('Desafio 4 - Calculadora')
    print ('-----------------------\n')

    if result is not None:
        print (f'{a_value} {operator_str} {b_value} = {result}')

    elif b_value is not None:
        print (f'{a_value} {operator_str} {b_value}')

    elif operator_str is not None:
        print (f'{a_value} {operator_str}')
    elif a_value is not None:
        print (f'{a_value}')


while True:
    monta_tela(None,None,None,None)
    a = float(input('\ndigite o primeiro termo: '))

    monta_tela(a,None,None,None)
    operator = input('digite o operador matemático: ')

    monta_tela(a,operator,None,None)
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
        monta_tela(a,operator,b,solution)

    repeat = 0

    while repeat != 'y' and repeat != 'n':
        monta_tela(a,operator,b,solution)
        repeat = input('Continuar? (y/n)')

    if repeat == 'n':
        break
