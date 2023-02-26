# Modulos em python (import, from, as, *)
# Modulos é a denominação para todos os arquivos python.
# Eles podem ser importados para que se possa usar as funções, classes e variaveis que existem dentro deles

# Como modulos são arquivos .py, alguns que por ficarem populares, por padrão, eles são instalados junto com o python.

# Qualquer um pode criar um modulo, mas aqui irei tratar só de como importa-los

# import nome_modulo => Importa o modulo inteiro
# Vantagens: Você tem o namespace do modulo protegendo os nomes dentro dele
# Por exemplo o modulo sys que possui a função plataform nele:

"""
import sys
print(sys.platform)
platform = "plataforma"
# é possivel usar a variavel platform sem afetar a função do modulo sys
"""

# Desvantagens: Nomes grandes
# Mas isso é considerado uma boa prática

# Outro exemplo usando o modulo time
import time

print("Eu estou aqui")

time.sleep(1) # O script espera por um segundo

# from nome_modulo import objeto => importa apenas o objeto do modulo

from os import system

system("clear") # Limpa a tela

# alias 1 => import nome_modulo as apelido
# o comando 'as' permite que você troque o nome do modulo por um apelido

import sys as s

sys = "Eu sou sys"

print(sys)
print(s.platform)

# alias 2 => from nome_modulo import objeto as apelido
# O comando 'as' tambem funciona com from

from random import randint as inteiro_aleatorio

numero_aleatorio = inteiro_aleatorio(1, 10)

print(numero_aleatorio)

# Vantagem: você pode reservar nomes para o seu codigo
# Desvantagem: fica fora dos padrões conhecidos na linguagem

# Má pratica!
# from nome_modulo import * => o * faz com que todos os nomes do modulo estajam disponiveis
# Vantagem: importa tudo do modulo
# Desvantagem: importa tudo do modulo

from decimal import *

print(Decimal)
print(DecimalException)
