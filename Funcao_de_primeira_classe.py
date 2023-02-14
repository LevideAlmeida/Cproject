"""
Funções de primeira classe
higher order functions => Funções que podem receber e/ou retornar outras funções
First-class function => Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""

def saudacao(msg, nome):
    return f'{msg} {nome}'

def executa(funcao, *args):
    return funcao(*args)

saudacao_2 = saudacao

v = executa(saudacao_2, 'boa noite', 'levi')
print(v)
