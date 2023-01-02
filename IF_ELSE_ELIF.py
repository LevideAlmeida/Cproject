# if / else / elif (else + if)
# se / se não / se não se
# if = se for algo, faça isso
# else = se não for esse algo, então faça isso
# elif = se não for esse algo, mas for essa outra coisa, faa isso

entrada = input("Entrar? (s/n) ")

if entrada == 's':
    print("Você entrou no sistema")
elif entrada == 'n':
    print("Você não entrou no sistema")
else:
    print("-_-")

"""
Para que o interpretador entenda que o codigo faz parte do bloco (if/else/elif), o codigo deve estar abaixo do bloco que com um espaço de tab.
Por exemplo:
if 0 == 0:
    "codigo"

O espaço que vem antes do codigo é o tamanho padrão da tecla tab
Qualquer codigo que venha depois do if/else/elif e não possiu um espaço de tab, acaba fechando o bloco e qualquer outro comando depois não é executado como parte disso
"""
