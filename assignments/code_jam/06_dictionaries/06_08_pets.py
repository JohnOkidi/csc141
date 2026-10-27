'''

John Okidi

learning one step at a time to get better
difficulty 8/10
'''

# Create dictionaries representing different pets
pet_1 = {
    'kind': 'dog',
    'owner': 'alice'
}

pet_2 = {
    'kind': 'cat',
    'owner': 'bob'
}

pet_3 = {
    'kind': 'parrot',
    'owner': 'charlie'
}

pet_4 = {
    'kind': 'hamster',
    'owner': 'david'
}
pets = [pet_1, pet_2, pet_3, pet_4]

# Loop through the list and print everything we know about each pet
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"This {kind} belongs to {owner.title()}.")