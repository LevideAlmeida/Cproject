def parameters_decorator(name):
    def decorator(func):
        print(f"Decorator: {name}")
        def iner_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {name}'
            return final
        return iner_function
    return decorator

@parameters_decorator(name='Fifth')
@parameters_decorator(name='Fourth')
@parameters_decorator(name='Third')
@parameters_decorator(name='Secund')
@parameters_decorator(name='First')
def multiplication(x,y):
    return x * y

ten_times_twelve = multiplication(10, 12)
print(ten_times_twelve)
