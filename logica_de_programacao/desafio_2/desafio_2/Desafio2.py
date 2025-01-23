from math import floor
import locale


locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def format_money(value):
    return locale.currency(value, grouping=True, symbol=True )

print ('-------------------------------')
print ('Desafio 2 - compra com desconto')
print ('-------------------------------\n\n'
       'Tecle Enter para concluir a compra\n')

shoppingCart = []
bill = 0

while True:
    
    item  = input('\nDigite o produto desejado: ').strip()
     
    if len(item) == 0:
        break

    price = input('Digite o valor do produto: ')
    if len(price) == 0:
        break

    price = float(price.replace(',','.'))
    if (price == 0):
        break


    quantity = input('Digite a quantidade desejada: ')
    if len(quantity) == 0:
        break

    quantity = floor(float(quantity.replace(',','.')))
    if quantity == 0:
        break


    if quantity > 50:
        discount = 0.75

    elif quantity > 20:
        discount = 0.80

    elif quantity > 10:
        discount = 0.90

    else:
        discount = 1

    value = price * quantity * discount
    bill += value

    shoppingCart.append(f'{quantity}x {item} - {format_money(price)} un. = {format_money(price * quantity)} \n'
                        f'Total do item: {format_money(value)} (Desconto: {1-discount:.0%})')

if len(shoppingCart) > 0:
    print ('\n\n---------------\n'
        ' CUPOM FISCAL\n'
        '---------------\n')

    for line in shoppingCart:
        print(line)

    print ('---------------')
    print(f'Valor total da nota: {format_money(bill)}')
else:
    print('Nenhum item foi adicionado ao carrinho. Tente novamente')