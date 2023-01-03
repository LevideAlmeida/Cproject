# Operadores lógicos
# and (e) or (ou) not (não)

"""
or - Apenas uma condição precisa ser verdadeira

Se uma das condições for verdadeira, a expressão como um todo será verdadeira
Se ambas as condições forem falsas, a expressão será falsa
"""

entrada = input("[E]ntrar [S]air ")
senha_digitada = input("Digite a senha: ")

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("Entrar")
else:
    print('Sair')

#É possivel usar esses operadores em uma variavel

Senha = input("senha: ") or 'Sem senha'
print(Senha)
