hora = input("Insira a hora (com numero inteiro): ")
hora_inteira = False
bom_dia = False
boa_tarde = False
boa_noite = False


try:
    hora = int(hora)
    hora_inteira = True

    if hora > 23:
        print('O horario não é valido')

except:
    print("Não foi inserido um Numero inteiro")

if hora_inteira:
    bom_dia = (hora >= 0 and hora < 12)
    boa_tarde = (hora >= 12 and hora <= 17)
    boa_noite = (hora >= 18 and hora <= 23)

if bom_dia:
    print("Bom dia")
elif boa_tarde:
    print("Boa tarde")
elif boa_noite:
    print("Boa noite")
