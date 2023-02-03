favorite_places = {'mark': ['zoo', 'club'], 'tom': ['aquarim', 'museum'], 'elizabeth': ['park']}
for name, places in favorite_places.items():
    for place in places:
        print(f"One of {name.title()}'s favorite place to visit is the {place}.")