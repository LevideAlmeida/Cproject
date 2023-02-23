# try, except
# Tratar erros que possam haver no codigo

a = 19
b = 'a'

try: # Executa o codigo
    print("Linha 1")
    c = a / b # Ocorreu erro no codigo

    # Essa parte não é executada
    print("Linha 2")
    print("Linha 3"[1000000])
    # print(b[1])

except ZeroDivisionError: # Caso esse seja o tipo do erro, execute o codigo abaixo:
    print("Dividiu por zero")
except (IndexError, NameError): # Caso o erro seja um desses 2 tipos, execute:
    print("IndexError ou NameError")
except TypeError as error: # Enviando o erro para uma variavel
    print("Mensagem de erro:", error) # A variavel contem a mensagem de erro
    print("Tipo do erro:", error.__class__.__name__) # Pegando o nome do erro dentro da variavel error
except Exception: # Exception se refere a todos os erros existentes, todo erro é uma exceção
    print("ERRO DESCONHECIDO")
