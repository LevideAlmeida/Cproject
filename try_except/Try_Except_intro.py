"""
Introdução ao try/except
try => Tenta executar o codigo
except => ocorreu um erro ao tentar executar
"""

numero_str = input("Digite um numero: ")

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f"o dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso não é um numero!")

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"o dobro de {numero_str} é {numero_float * 2:.2f}")
# else:
#     print("Isso não é um numero!")
