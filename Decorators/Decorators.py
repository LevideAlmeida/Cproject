# Decorator functions and decorators
# Decorate = add / remove / restrict / change
# Decorator functions are functions that decorate others functions
# Decorators are used to do the python use the decorator function in others functions

# Decorator function
def create_function(function):
    def internal_function(*args, **kwargs):
        print('I will decorate you')
        for arg in args:
            is_string(arg) #Restrict
        result = function(*args, **kwargs)
        result += "By decorator" # Add
        print(f'the result is {result}')
        print('You be decored')
        return result
    return internal_function

def is_string(arg):
    if not isinstance(arg, str):
        raise TypeError("arg must be a str")

@create_function # Syntax_sugar
def invert_string(string):
    print(invert_string.__name__) # is not anymore invert_string function
    return string[::-1]

inverted_string = invert_string('123')
print(inverted_string)

"""
Normally you have use this code to use the decorator function:
# invert_str_checking_if_arg_is_a_str = create_function(invert_string)
# variable = '123'
# print(invert_str_checking_if_arg_is_a_str(variable))
but, with decorator and your syntax_sugar, is possible simplify the code
using @decorator_function before def function
when you use the function, it be used how argument to decorator_function.
Now the function do not exists anymore, then decorator function always be executed
"""
