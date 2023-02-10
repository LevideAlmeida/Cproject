# Calculo do primeiro dígito do CPF
import re

CPF = input("Digite o CPF: ")

cpf_enviado_usuario = re.sub(r'[^0-9]', '', CPF)

cpf_e_sequencial = CPF == CPF[0] * len(CPF)

if cpf_e_sequencial:
    print("CPF invalido por repetição!!!")
    exit()

nove_digitos = cpf_enviado_usuario[0:9]
multiplicador_regressivo = 10
soma = 0

for numero in nove_digitos:
    soma += int(numero) * multiplicador_regressivo
    multiplicador_regressivo -= 1

primeiro_digito = (soma * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# Calculo do segundo dígito do CPF

dez_digitos = nove_digitos + str(primeiro_digito)
multiplicador_regressivo = 11
soma = 0

for digito in dez_digitos:
    soma += int(digito) * multiplicador_regressivo
    multiplicador_regressivo -= 1

segundo_digito = (soma * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{CPF} é valido')

else:
    print("CPF invalido!!!")
