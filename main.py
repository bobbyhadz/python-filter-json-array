# How to filter a JSON array in Python

import json

json_array = json.dumps(
    [
        {'name': 'Alice', 'salary': 100},
        {'name': 'Bobby', 'salary': 50},
        {'name': 'Carl', 'salary': 75}
    ]
)

a_list = json.loads(json_array)

filtered_list = [
    dictionary for dictionary in a_list
    if dictionary['salary'] > 50
]

# 👇️ [{'name': 'Alice', 'salary': 100}, {'name': 'Carl', 'salary': 75}]
print(filtered_list)