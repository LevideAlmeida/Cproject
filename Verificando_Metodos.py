# dir, getattr, hasattr

string = 'Levi'
metodo = 'upper'
if hasattr(string, metodo):
    print(f"Exite metodo {metodo}")
    print(getattr(string, metodo)())
else:
    print(f'Não exite o metodo {metodo}')
