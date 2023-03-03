separator = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


def function_factory(func):
    def iner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return iner_function

@function_factory  # Applying decorator in the multiplication function
def multiplication(x, y):
    return x * y


five_times_ten = multiplication(5, 20)
print(five_times_ten)

#####################################################


def print_a_b_c(a, b, c):
    print(a, b, c)
    return function_factory


@print_a_b_c(1, 2, 3)  # sending parameters to function print_a_b_c
# The function is executed imediataly when called with @
def inter_division(x, y):
    return x // y


sixty_six_divided_by_six = inter_division(66, 6)
print(sixty_six_divided_by_six)

###########################################################

potentiation = function_factory(lambda x, y: x ** y)
# Using lambda to create a function with decorator(functions_factory)

four_cubed = potentiation(4, 3)
print(four_cubed)

##########################################################
print(separator)

def decorator_factory(a=None, b=None, c=None):
    def function_factory(func):
        def iner_function(*args, **kwargs):
            print(f'Parameters of decorator: {a,b,c}')
            result = func(*args, **kwargs)
            return result
        return iner_function
    return function_factory

decorator = decorator_factory(a='a', b='b', c='c')
subtraction = decorator(lambda x,y: x-y)

five_minus_ten = subtraction(5, 10)
print(five_minus_ten)
