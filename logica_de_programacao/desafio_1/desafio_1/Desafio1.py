import json
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def format_money(value):
    return locale.currency(value, grouping=True, symbol="R$" )

with open("productStock.json", encoding="UTF-8") as productStock:
    stockItems = json.load(productStock)

cartValue = 0

print ('\n'
       '-------------------------------------------------------------------------------------------------')

for item in stockItems:

    itemValue = (item.get('quantidade') * item.get('preco'))
    
    print(f'Item: {item.get("nome").rjust(15)} | '
          f'quantidade: {str(item.get("quantidade")).rjust(6)} | '
          f'preço: {str(format_money(item.get('preco'))).rjust(12)} | '
          f' Total do item:    {str(format_money(itemValue)).ljust(10)}'
          )
    print ('-------------------------------------------------------------------------------------------------')

    cartValue += itemValue


print ('\n'
       f'Valor total dos itens estoque: {format_money(cartValue)}'
       '\n'
       '\n' )
