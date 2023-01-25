# Calculadora com while

while True:

    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+ - / *): ")

    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True
    except:
        print("ERRO! Todos ou algum dos valores é invalido")

    if numeros_validos is None:
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("ERRO! O operador é invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador")
        continue

    if operador == '+':
        resultado = numero_1 + numero_2
        print(resultado)
    elif operador == '-':
        resultado = numero_1 - numero_2
        print(resultado)
    elif operador == '*':
        resultado = numero_1 * numero_2
        print(resultado)
    elif operador == '/':
        resultado = numero_1 / numero_2
        print(resultado)

    sair = input("Sair? [s]im: ").lower().startswith('s')

    if sair == True:
        break
