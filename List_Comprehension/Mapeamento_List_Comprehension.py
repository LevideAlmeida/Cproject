# Mapeamento de dados com List Comprehension
# Mapear uma lista é criar outra lista a partir da mesma e manter a mesma quantidade de itens

preco_produtos = [
    {'produto1': 'pão', 'preço': 6.50,},
    {'produto2': 'arroz', 'preço': 5,},
    {'produto3': 'frango(kg)', 'preço': 30},
    {'produto4': 'coca-cola', 'preço': 10,},
    ]

#Preços com aumento de 5% caso o preço seja maior que 20
novos_precos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto}
    for produto in preco_produtos
]

print(*novos_precos, sep='\n')
