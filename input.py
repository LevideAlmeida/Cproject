#Pegando o nome do usuarios
nome = input("Qual o seu nome? ")

#Imprimindo o nome
print(f'O seu nome é {nome}')

#A função input sempre retorna uma função str
numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

#Transformando os numeros que estão como str em variaveis int
int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

"""
Se o usuarios digitar algo que não seja um numero, acontecerá um erro, pois converter letras em int, é impossivel. Usando funções condicionais, é possivel evitar isso, no futuro veremos sobre elas

"""

print("A soma dos números é igual a", {int_numero1 + int_numero2})
