# Operadores lógicos
# and (e) or (ou) not (não)

"""
and - Todas as condições precisam ser
verdadeiras.
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados falsy (valores falsos)
0 / 0.0 / '' / False
Também existe o tipo None que é
usado para representar um não
"""

# entrada = input("[E]ntrar [S]air ")
# senha_digitada = input("Digite a senha: ")

# senha_permitida = '123456'

# if entrada == 'E' and senha_digitada == senha_permitida:
#     print("Entrar")
# else:
#     print('Sair')


print(True and True and True) #Retorna True
print(True and False and True and True and True and True) #Retorna False
print(bool(0)) #Retorna False
print(True and 0 and True) #Retorna 0 (false)
