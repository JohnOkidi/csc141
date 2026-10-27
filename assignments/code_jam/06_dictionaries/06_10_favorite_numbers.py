'''


John Okidi
Python is dangerous
difficulty 5/10

'''

# A dictionary storing multiple favorite numbers for five people
favorite_numbers = {
    'Sarah': [7, 21, 35],
    'Jordan': [42, 84],
    'Maya': [13, 7, 9],
    'Liam': [3, 6, 9, 12],
    'Alex': [99, 100]
}

# Print each person's name and their favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")