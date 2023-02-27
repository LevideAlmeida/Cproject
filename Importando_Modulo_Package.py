print(__name__)


from python_package.Modulo_a import sum_of_module

print(sum_of_module(1, 2))

import python_package.Modulo_b

print(python_package.Modulo_b.division_of_module(10, 2))
print(python_package.Modulo_b.name_module_b)

from python_package.Modulo_a import name_module_a

print(name_module_a)
