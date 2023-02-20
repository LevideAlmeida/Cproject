import os

palavra_secreta = "cadeira"
palavra_formatada = ""
tamanho_da_palavra = len(palavra_secreta)
tentativas = 0

for i in palavra_secreta:
    palavra_formatada += "*"

while "*" in palavra_formatada:
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if not letra_digitada:
        print("Palavra Formatada:", palavra_formatada)
        continue

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue

    nova_palavra_formatada = ""

    for j in range(tamanho_da_palavra):
        if letra_digitada in palavra_secreta[j]:
            nova_palavra_formatada += letra_digitada
        else:
            nova_palavra_formatada += palavra_formatada[j]
    palavra_formatada = nova_palavra_formatada
    print("Palavra Formatada:", palavra_formatada)

os.system('reset')
print("PARABENS!!! VOCÊ GANHOU!!!")
print(f"Numero de tentativas: {tentativas}")
