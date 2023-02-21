# isinstance() => é para saber se um objeto é de um determinado tipo

lista = [1, True, {3, 4}, 5.6,
         'levi', {'nome': 'levi'}, {1 ,6}
        ]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item)

    elif isinstance(item, str):
        print("STR")
        print(item.upper())

    elif isinstance(item, (int, float)):
        print("NUM")
        print(item, item * 2)

    else:
        print("OUTRO")
        print(item)

    print()
