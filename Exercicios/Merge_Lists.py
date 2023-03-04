# Exercises - fusion lists
# make a zipper function
# The job of this function is to join two lists in order.
# Use all values of minor list.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Result
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
separator = '----------------------------------------'

# My first solution for exercise
city_list = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Fortaleza']
states_list = ['BA','SP','MG']

def zipper(list_a, list_b):
    new_list = []
    for i, item in enumerate(list_a):
        new_list.append((item, list_b[i]))
    return new_list

zip_list = None
if len(city_list) > len(states_list):
    zip_list = zipper(states_list, city_list)
else:
    zip_list = zipper(city_list, states_list)

print(zip_list)

#############################################################

print(separator)

# New solution using teacher correction
def zipper(list_a, list_b):
    new_list = []
    minor_list = min(len(list_a), len(list_b))
    for i in range(minor_list):
        new_list.append((list_a[i], list_b[i]))
    return new_list

new_list = zipper(city_list, states_list)
print(new_list)

###########################################################

print(separator)

# The purpose of exercise is for you learn the logic behind this code
# But python have a class for this

print(zip(city_list, states_list))
new_list = list(zip(city_list, states_list))
print(new_list)

print(separator)

# There is also a class in the module intertools that does this using all values from the larger list
from itertools import zip_longest

print(zip_longest(city_list, states_list))
new_list = list(zip_longest(city_list, states_list))
print(new_list)

# As this function uses indexes of the largest list, when creating tuples, the excedents values receive None as duple in the tuple
# Exemple: (None, 'RJ')
# It's possible change this using fillvalue keyword argument
print(separator)

new_list = list(zip_longest(city_list, states_list, fillvalue='No state'))
print(new_list)
