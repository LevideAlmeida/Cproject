import random

for _ in range(100):

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    multiplicador_regressivo = 10
    soma = 0

    for numero in nove_digitos:
        soma += int(numero) * multiplicador_regressivo
        multiplicador_regressivo -= 1

    primeiro_digito = (soma * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    dez_digitos = nove_digitos + str(primeiro_digito)
    multiplicador_regressivo = 11
    soma = 0

    for digito in dez_digitos:
        soma += int(digito) * multiplicador_regressivo
        multiplicador_regressivo -= 1

    segundo_digito = (soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    print(cpf_gerado_pelo_calculo)
