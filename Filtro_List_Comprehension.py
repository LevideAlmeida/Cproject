# Filtro de dados com List Comprehension
# Filtrar uma lista é criar uma nova lista a partir da mesma, mas retirando elementos indesejados

lista = [n for n in range(10) if n < 5]
print(lista)

preco_produtos = [
    {'produto1': 'pão', 'preço': 6.50,},
    {'produto2': 'arroz', 'preço': 5,},
    {'produto3': 'frango(kg)', 'preço': 30},
    {'produto4': 'coca-cola', 'preço': 10,},
    ]

precos_maior_ou_igual_que_10 = [
    produto for produto in preco_produtos
    if produto['preço'] >= 10
]

print(*precos_maior_ou_igual_que_10, sep="\n")
