from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'name': 'product 1', 'price': 10.00},
    {'name': 'product 2', 'price': 22.22},
    {'name': 'product 3', 'price': 10.11},
    {'name': 'product 4', 'price': 105.87},
    {'name': 'product 5', 'price': 69.90},
]

def increase_percentage(value, percent):
    return round(value + (value * percent / 100), 2)

increase_ten_percent = partial(
    increase_percentage,
    percent=10
)

# new_products  = [
    # {**p, 'price': increase_ten_percent(p['price'])}
    # for p in products
# ]

def change_products_price(product):
    return {**product, 'price': increase_ten_percent(product['price'])}


new_products = map(
    change_products_price,
    products
    )

print_iter(products)
print_iter(new_products)

print(new_products)
print(hasattr(new_products, '__iter__'))
print(hasattr(new_products, '__next__'))

from types import GeneratorType

new_products = (x for x in products)

print(isinstance(new_products, GeneratorType))

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
    )
