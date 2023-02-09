"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
condicao_true = 10 == 10
condicao_false = 10 > 10
variavel_True = 'Valor' if condicao_true else 'Outro Valor'
variavel_False = 'Valor' if condicao_false else 'Outro Valor'

print(variavel_True)
print(variavel_False)



digito = 9
novo_digito = digito if digito <= 9 else 0

print(novo_digito)
