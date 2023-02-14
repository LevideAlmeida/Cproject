# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Levi',
#     'sobrenome': 'Almeida',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Levi', sobrenome='Almeida')

pessoa = {
    'nome': 'Levi',
    'sobrenome': 'Almeida',
    'idade': 18,
    'altura': 1.75,
    'peso(kg)': 60,
    'endereços': [
        {'rua': 422, 'numero': 129},
        {'rua': 224, 'numero': 921},
    ]
}
# pessoa = dict(nome='Levi', sobrenome='Almeida')

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])
