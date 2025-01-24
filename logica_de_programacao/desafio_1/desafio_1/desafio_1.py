"""Lê os dados de um JSON e calcula o valor total do estoque"""
import json
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def format_money(value):
    """Retorna strung com formatação de BRL"""
    return locale.currency(value, grouping=True, symbol=True )

with open("productStock.json", encoding="UTF-8") as productStock:
    stockItems = json.load(productStock)

cart_value = 0

print ('\n'
       '------------------------------------------------------------------------------------------')

for item in stockItems:

    item_value = (item.get('quantidade') * item.get('preco'))

    print(f'Item: {item.get("nome").rjust(15)} | '
          f'quantidade: {str(item.get("quantidade")).rjust(6)} | '
          f'preço: {str(format_money(item.get('preco'))).rjust(12)} | '
          f' Total do item:    {str(format_money(item_value)).ljust(10)}'
          )
    print ('--------------------------------------------------------------------------------------')

    cart_value += item_value


print ('\n'
       f'Valor total dos itens estoque: {format_money(cart_value)}'
       '\n'
       '\n' )
