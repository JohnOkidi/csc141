'''

I hate doing homework but python is fun


'''
my_foods = ['pizza', 'chicken', 'brownies']
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('cookies')
print("My favorite foods are:")
for food in my_foods:
    print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)