#Tipos de dados

'''
str -> string -> texto
strings são textos que estão dentro de aspas
print("hello world")
print('hello world')
'''

#aspas duplas
print("Hello world")

#aspas simples
print('Hello world')

#escape
print("Hello \"world\"")
"""

a barra invertida (\) pode ser usado como escape para que o programa
não interprete o proximo caractere como parte do codigo e o encare como string

"""

#r
print(r"Hello \"world\"")
"""

é o escape do caractere de escape, mas originalmente é pra ser usado em expressões regulares

"""

#Mas para que complicar sendo que se pode simplesmente colocar aspas simples e depois duplas?
print('Hello "world"')
#e vice versa
print("Hello 'world'")

"""
Tipos de numeros
int = inteiro
float = numeros "quebrados"/decimais
"""

#int
print(1234) #inteiro
print(-4321) #interio negativo

#float
print(5.5, 2.2) #Numeros decimais são separados por pontos e não por virgulas
print(0.0, -3.3)

# type() Mostra o tipo do argumento
print(type('Levi')     )
print(type(0), type(11), type(-11))
print(type(0.0), type(1.1), type(-1.1))
