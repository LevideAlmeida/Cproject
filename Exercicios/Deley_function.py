def sum(x, y):
    return x + y

def multiplication(x,y):
    return x * y

def create_funcition(function, x):
    def internal_function(y):
        return function(x, y)
    return internal_function

sum_with_five = create_funcition(sum, 5)
multiplicate_by_ten = create_funcition(multiplication, 10)

print(sum_with_five(5))
print(multiplicate_by_ten(10))
