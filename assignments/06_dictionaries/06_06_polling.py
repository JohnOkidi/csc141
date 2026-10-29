'''

John okidi
pyhton is godly
difficulty 7/10

'''

# The favorite_languages dictionary from the book example
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# A list of people who should take the poll
poll_participants = ['jen', 'edward', 'matt', 'sarah', 'chloe', 'phil', 'michael']

# Loop through the list of participants
for name in poll_participants:
    if name in favorite_languages:
        print(f"Thank you, {name.title()}, for taking the poll!")
    else:
        print(f"Hi {name.title()}, please take our favorite languages poll!")