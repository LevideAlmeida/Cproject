# Iterando strings com while

nome = "Levi de Almeida"

tamanho_nome = len(nome)

nova_string = ""
cont = 0
while cont < tamanho_nome:
    nova_string += f"{nome[cont]}-"
    cont += 1

print(nova_string)
