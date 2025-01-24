"""Calcula a comissão a ser repassada ao corretor de imóveis por suas vendas"""
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def format_money(value):
    """Retorna strung com formatação de BRL"""
    return locale.currency(value, grouping=True, symbol=True )

print ('-----------------------------------')
print ('Desafio 5 - Calculadora de comissão')
print ('-----------------------------------\n')

name = input('\ndigite nome do vendedor: ')

sell_value = float(input('digite o valor da venda do imóvel: '))


if sell_value >= 50000:
    commission = sell_value*0.20

elif sell_value >= 30000:
    commission = sell_value*0.15

else:
    commission = sell_value*0.10


print (f'Vendedor: {name}. '
       f'Valor do imóvel: {format_money(sell_value)} '
       f'Comissão: {format_money(commission)}.')
