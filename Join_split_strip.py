"""
Metodos para list e str
split - separa uma string
join - une uma string
strip - apaga os espaços do começo e do fim da str
"""

frase = "     Olha só    ,   que coisa interessante   "
lista_palavras = frase.split()
print(lista_palavras)

lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)
frases_unidas = "-".join(lista_frases)
print(frases_unidas)
