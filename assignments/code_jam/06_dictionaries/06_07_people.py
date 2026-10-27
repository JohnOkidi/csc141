'''


John Okidi

Python may justv rule the world. im struggling at times though

'''
# Dictionary for the first person
person_1 = {
    'first_name': 'Alex',
    'last_name': 'Smith',
    'age': 16,
    'city': 'Seattle'
}

# Two new dictionaries for different people
person_2 = {
    'first_name': 'Elena',
    'last_name': 'Garcia',
    'age': 17,
    'city': 'Austin'
}

person_3 = {
    'first_name': 'Marcus',
    'last_name': 'Johnson',
    'age': 15,
    'city': 'Chicago'
}

# Store all three dictionaries in a list called people
people = [person_1, person_2, person_3]

# Loop through the list of people and print everything we know about each person
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Name: {full_name}")
    print(f"  Age: {age}")
    print(f"  City: {city}\n")