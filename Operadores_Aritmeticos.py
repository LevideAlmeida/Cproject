# Operadores Matematicos

adicao = 10 + 10
print("Adição:", adicao)

subtracao = 30 - 17
print("Subtração:", subtracao)

multiplicacao = 10 * 10
print("Multiplicação:", multiplicacao)

divisao = 20 / 1.1 # Sempre retorna float
print("Divisão:", divisao)

divisao_inteira = 20 // 1.1 # O resultado sempre retorna um numero inteiro ou um float com (.0)
print("Divisão inteira:", divisao_inteira)

exponenciacao = 2 ** 10
print("Exponenciação:", exponenciacao)

modulo = 55 % 2 # é o resto da divisão
print("Modulo:", modulo)

# Peculiaridades de operadores

# Ao se somar caracteres usando o operador (+), esses caracteres serão concatenados (juntados)

concatenacao = 'Levi' + ' ' + 'Almeida'
print("Concatenação:", concatenacao)

# Ao se multiplicar strings com um numero inteiro, isso ira gerar a repetição da string tantas vezes quando o valor do inteiro

a_dez_vezes = 'A' * 10
levi_tres_vezes = 'Levi' * 3
print(a_dez_vezes)
print(levi_tres_vezes)
