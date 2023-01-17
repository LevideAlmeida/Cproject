nome = input("Digite o seu primeiro nome: ")

if len(nome) > 1:
    if len(nome) < 5:
        print("Seu nome é curto")
    elif len(nome) > 4 and len(nome) < 7:
        print("Seu nome é normal")
    elif len(nome) > 6:
        print("Seu nome é grande")
else:
    print("Digite mais de uma letra")
