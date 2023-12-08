import json
customers = []
with open('./5784_jsonl/noahs-customers.jsonl') as f:
    for line in f:
        customers.append(json.loads(line))
print(len(customers))

# customers = [
#     {"name": "Noah", "phone": "555"},
# ]

keypad = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ'
}

for customer in customers:
    possible_names = [""]
    for num in customer['phone']:
        if num in keypad:
            next_possible_names = []
            for char in keypad[num]:
                for name in possible_names:
                    next_possible_names.append(name + char)
            possible_names = next_possible_names
    for name in possible_names:
        if name.lower() in customer['name'].lower():
            print(name, customer['name'], customer['phone'])
