# Exercises
# increase prices of products to follow in ten percent
# Generate new_products by deep copy
separator = "------------------------------------"

import copy

products = [
    {'name': 'Product 5', 'price': 10.00},
    {'name': 'Product 1', 'price': 22.32},
    {'name': 'Product 3', 'price': 10.11},
    {'name': 'Product 2', 'price': 105.87},
    {'name': 'Product 4', 'price': 69.90},
]

new_products = copy.deepcopy(products)

for product in new_products:
    ten_percent_product = round(0.1 * product['price'], 1)
    product['price'] += ten_percent_product

print(*new_products, sep='\n')

print(separator)

# sort the products by name decrescent (from bigger to minor)
# Generate products_sorted_by_name by deep copy

products_sorted_by_name = copy.deepcopy(new_products)
products_sorted_by_name.sort(reverse= True, key=lambda produto: produto['name'])
print(*products_sorted_by_name, sep='\n')

print(separator)

# sort the products by price crescent (from minor to bigger)
# Generate products_sorted_by_price by deep copy

products_sorted_by_price = copy.deepcopy(new_products)
products_sorted_by_price.sort(key=lambda product: product['price'])
print(*products_sorted_by_price, sep='\n')
