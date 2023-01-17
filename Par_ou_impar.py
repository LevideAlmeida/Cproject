numero_str = input("Digite um numero Inteiro: ")
is_a_number_int = False
par_ou_impar = False # True => par / False => impar

try:
    numero_int = int(numero_str)
    is_a_number_int = True # O numero é inteiro
    par_ou_impar = (numero_int % 2) == 0
except:
    print("Esse não é um numero inteiro")

Verifica_se_e_par_ou_impar = is_a_number_int and par_ou_impar

if Verifica_se_e_par_ou_impar:
    print(f"O numero {numero_int} é par")
elif par_ou_impar:
    print(f"O numero {numero_int} é impar")
