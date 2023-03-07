# Math topics
# Permutations => order is important. Equals combinations, but in diferent positions

from itertools import permutations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

people = ['Eduarda', 'Vitoria', 'Anne', 'Luzia']

people_permutations = permutations(people, 2)
print_iter(people_permutations)
