'''

John Okidi
Im struggling to keep up at times
difficulty 7/10
'''

cities = {'chicago' : {'country': 'USA', 'population' : 2716000 , 'fact' : 'known for its windy climate'}}


# Print the name of each city and its information
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']

    print(f" {city.title()} is in {country}.")
    print(f" it has a population of {population}.")
    print(f"fun fact: {fact}\n")