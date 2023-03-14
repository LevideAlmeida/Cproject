# json is a file type
# is useful to save datas externally

# to use functions for json, import json module
import json

# A person's personal informations
person = {
    'name': 'Levi',
    'surname': 'Almeida',
    'adresses': [
        {'street': 422, 'house': 129},
        {'street': 224, 'house': 921},
    ],
    'height': 1.70,
    'preferred_numbers': (2, 5, 10, 24, 69),
    'dev': True,
    'None': None,
}

with open('people.json', 'w') as file:
    # Transfer person dictionary for file
    json.dump(person, file, indent=2)
    # 🚸CAUTION🚸: json files do not suport all datas type, as set for exemple

with open('people.json', 'r') as file:
    # Import data from external file
    person = json.load(file)
    print(person)
    print(type(person))
