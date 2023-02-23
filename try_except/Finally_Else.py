try:
    print("ABRIR ARQUIVO")
    8/0 #Erro
except ZeroDivisionError:
    print("Dividiu por zero")
finally: # Vai ser executado de qualquer maneira, tendo erro ou não
    print("FECHAR ARQUIVO")


try:
    a = 1 + 1
except TypeError:
    print("TypeError")
else:
    print("NÃO HOUVE ERROS")
