price = input('price:')

try:
    price = float(price)
    print('price=', price)
except ValueError:
    print('not a number!')
