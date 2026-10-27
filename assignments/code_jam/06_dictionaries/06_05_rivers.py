'''

John Okidi
python is a mystery
difficulty 8/10

'''
# Create a dictionary of major rivers and the countries they run through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 1. Print a sentence about each river
print("--- River Sentences ---")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 2. Print the name of each river
print("\n--- Rivers Included ---")
for river in rivers.keys():
    print(river.title())

# 3. Print the name of each country
print("\n--- Countries Included ---")
for country in rivers.values():
    print(country.title())