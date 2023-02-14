# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

numeros_multiplicados = multiplicar(3,4,5,6,7)
print(numeros_multiplicados)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
    if (numero % 2) == 0:
        return f'{numero} é par'
    return f'{numero} é impar'

import random
numero = random.randint(0, 100)
par_impar = par_ou_impar(numero)

print(par_impar)
