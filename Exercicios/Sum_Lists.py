# Considering two lists of int or float (list_a and list_b)
# Sum the lists values and return a new list with sum values
# If a list is greater than orther, use the values from the smallest
# Exemple:
# list_a = [1, 2, 3, 4, 5, 6, 7, 8]
# list_b = [1, 2, 3, 4]
# Result:
# new_list = [2, 4, 6, 8]

def sum_lists(list_a, list_b):
    small_list = list_a

    if len(list_a) < len(list_b):
        small_list = list_a
    else:
        small_list = list_b

    print(small_list)

    new_list = []
    for i, _ in enumerate(small_list):
        new_list.append(list_a[i] + list_b[i])
    return new_list


list_a = [1, 2, 3, 4, 5, 6, 7, 8]
list_b = [1, 2, 3, 4]

sum_list = sum_lists(list_b, list_a)
print(sum_list)

list_c = [5, 6, 7, 8]
list_d = [1, 6, 9, 3, 5, 2]

sum_list = sum_lists(list_d, list_c)
print(sum_list)
