import math

def convert_str_in_float(variable):
    try:
        float_variable = float(variable)
    except ValueError:
        raise

    return float_variable

def resolving_equation(a, b, c):
    delta = (b ** 2) - 4 * a * c
    try:
        square_root_delta = math.sqrt(delta)
    except ValueError:
        return 'NÃO EXISTEM VALORES POSSÍVEIS'

    resolve_with_plus = (-b + square_root_delta) / (2 * a)
    resolve_with_minor = (-b - square_root_delta) / (2 * a)
    result = {resolve_with_plus, resolve_with_minor}
    return tuple(result)

print("Second degree equation: ")
print("Form: ax² + bx + c = 0")
print("a ≠ 0; a, b and c is an int\n")

a = input("Insert a: ")
a = convert_str_in_float(a)

b = input("Insert b: ")
b = convert_str_in_float(b)

c = input("Insert c: ")
c = convert_str_in_float(c)

x = resolving_equation(a, b, c)

print(x)
