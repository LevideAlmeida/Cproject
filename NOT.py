# Operadores lógicos
# and (e) or (ou) not (não)

'''
Operador not:
significa literalmente, não é algo
é usado para inverter expressões
exemplo:
not true = false
not false = true
'''

print(not False)
print(not True)

senha = input("Senha: ")

if not senha:
    print("Você não digitou nada")
elif senha == '123456':
    print("Senha correta")
