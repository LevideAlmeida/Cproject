# raise - Lançando erros
# raise NameError("Lançando erro desnecessario")
"""
Um exemplo bem bruto de codigo com raise

def divide(numero, divisor):
    try:
        return numero / divisor
    except ZeroDivisionError:
        print("Fiz algo com o erro")
        raise # Relança o erro que foi tratado no except

print(divide(8, 1))

"""
# Um exemplo melhor e mais pratico para se usar raise

def can_not_be_zero(divisor):
    if divisor == 0:
        raise ZeroDivisionError("Não é possivel dividir por zero")
    return True

def must_be_an_int_or_float(value):
    type_value = type(value)
    if not isinstance(value, (float, int)):
        raise TypeError(
            f"{value} Deve ser int ou float."
            f' "{type_value.__name__ }" enviado.'
        )
    return True

def division(number, divider):
    can_not_be_zero(divider)
    must_be_an_int_or_float(number)
    must_be_an_int_or_float(divider)

    return number / divider

print(division(3, '0'))
