from functools import reduce

products = [
    {'name': 'product 1', 'price': 10.00},
    {'name': 'product 2', 'price': 22.22},
    {'name': 'product 3', 'price': 10.11},
    {'name': 'product 4', 'price': 105.87},
    {'name': 'product 5', 'price': 69.90},
]

# def function_of_reduce(acumulator, product):
    # print('acumulator', acumulator)
    # print('product', product)
    # print()
    # return acumulator + product['price']

total = reduce(
    lambda ac, p: ac + p['price'],
    products,
    0
)

print('Total is', total)

# acumulator = 0
# for p in products:
#     acumulator += p['price']

# print(acumulator)

# print(sum([p['price'] for p in products]))
