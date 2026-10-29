'''

Python
John Okidi

difficulty 7/10
'''

# Create a dictionary storing favorite numbers for five people
favorite_numbers = {
    'Sarah': 7,
    'Jordan': 42,
    'Maya': 13,
    'Liam': 3,
    'Alex': 99
}

# Print each person's name and their favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")