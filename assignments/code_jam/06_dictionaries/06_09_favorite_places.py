'''

John Okidi 
Python is key to world domination. stil struggling at times.
difficulty 6/10\
    
'''

# Create a dictionary where each key maps to a list of favorite places
favorite_places = {
    'sofia': ['paris', 'hawaii', 'tokyo'],
    'liam': ['grand canyon'],
    'maya': ['new york', 'yellowstone']
}
for name, places in favorite_places.items():
    # Handle grammar based on whether the person has 1 or multiple places
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    
   
    for place in places:
        print(f"  - {place.title()}")