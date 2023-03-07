# Math topics
# Product

from itertools import product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

t_shirts = [
    ['black', 'white'],
    ['p', 'm', 'g', 'gg'],
    ['masculine', 'feminine', 'unisex'],
    ['cotton', 'felt']
]

print_iter(product(*t_shirts))
