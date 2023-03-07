# Math topics
# Combinations => no matching combinations, the order doesn't matter

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

from itertools import combinations

people = ['Levi', 'Pedro', 'Policarpo', 'Eric']

print(combinations(people, 2))
people_combinations_in_groups_of_two = combinations(people, 2)
people_combinations_in_groups_of_three = combinations(people, 3)
print_iter(people_combinations_in_groups_of_two)
print_iter(people_combinations_in_groups_of_three)
