# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
separator = "-------------------------------------"

import copy

products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

new_products = copy.deepcopy(products)

for product in new_products:
    ten_percent_product = round(0.1 * product['preco'], 1)
    product['preco'] += ten_percent_product

print(*new_products, sep='\n')

print(separator)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

products_sorted_by_name = copy.deepcopy(new_products)
products_sorted_by_name.sort(reverse= True, key=lambda produto: produto['nome'])
print(*products_sorted_by_name, sep='\n')

print(separator)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

products_sorted_by_price = copy.deepcopy(new_products)
products_sorted_by_price.sort(key=lambda product: product['preco'])
print(*products_sorted_by_price, sep='\n')
