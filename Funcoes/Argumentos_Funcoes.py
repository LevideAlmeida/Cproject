"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x = } {y = } {z = }', '|', 'x + y =', x + y)

# Argumento Não Nomeado
soma(1, 2, 3)

# Argumento Nomeado
soma(y = 2, z = 3, x = 1)
