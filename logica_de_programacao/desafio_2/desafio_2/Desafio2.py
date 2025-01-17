import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

def format_money(value):
    return locale.currency(value, grouping=True, symbol="R$" )

print ('-------------------------------')
print ('Desafio 2 - compra com desconto')
print ('-------------------------------\n\n'
       'Tecle Enter para concluir a compra\n')

shoppingCart = []
bill = 0

while True:
    
    getItem  = input('\nDigite o produto desejado: ')
    item = getItem.strip()

    if len(getItem) == 0:
        break

    getPrice = input('Digite o valor do produto: ')
    if (len(getPrice) == 0):
        break

    price = float(getPrice.replace(',','.'))
    if (price == 0):
        break


    getQuantity = input('Digite a quantidade desejada: ')
    if len(getQuantity) == 0:
        break

    quantity = int(getQuantity.replace(',','.'))
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