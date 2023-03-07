# groupby => grouping values

from itertools import groupby
from copy import deepcopy

students = [
    {'name': 'Levi', 'grade': 'A'},
    {'name': 'Breno', 'grade': 'C'},
    {'name': 'Luzia', 'grade': 'C'},
    {'name': 'Pedro', 'grade': 'B'},
    {'name': 'Eduarda', 'grade': 'B'},
    {'name': 'Vitoria', 'grade': 'A'},
    {'name': 'Anne', 'grade': 'A'},
    {'name': 'VitoriaK', 'grade': 'C'},
    {'name': 'Matheus', 'grade': 'C'},
    {'name': 'Eric', 'grade': 'C'},
    {'name': 'Rian', 'grade': 'E'},
]

def sort(student):
    return student['grade']

sorted_students = deepcopy(sorted(students, key=sort))
groups = groupby(sorted_students, key=sort)

for key, group in groups:
    print(key)
    for student in group:
        print(student)
