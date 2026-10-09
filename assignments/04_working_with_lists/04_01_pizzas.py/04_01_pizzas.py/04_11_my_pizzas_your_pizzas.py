''' 


hard work for chapter 4 assignment 11

'''
# start with orginal list of pizzas
pizzas = ['pepperoni', 'hawaiian', 'veggie']

# make a copy of the list using slice
friend_pizzas = pizzas[:]

# add new pizzaa to orginal list
pizzas.append('cheese')

friend_pizzas.append('bbq chicken')
# Print favorite pizza using loop
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)