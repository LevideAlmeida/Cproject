"""
Introdução às funções em Python

Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.

Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.

Por padrão, funções Python retornam None (nada).

(def) define uma função
"""
def contar(numero_1, numero_2):
    for numero in range(numero_1, numero_2 + 1):
        print(numero)

def saudacao(nome="Sem nome"):
    print(f'Olá, {nome}')

saudacao()

nome = input("Insira um nome: ")

saudacao(nome)

numero_1 = input("Insira o primeiro numero da contagem: ")
numero_2 = input("Insira o ultimo numero da contagem: ")
contar(int(numero_1), int(numero_2))
