pet_0 = {'animal': 'cat', 'owner': 'Stan', 'duration': 4}
pet_1 = {'animal': 'dog', 'owner': 'Joseph', 'duration': 8}
pet_2 = {'animal': 'hamster', 'owner': 'Daniel', 'duration': 2}
people = [pet_0, pet_1, pet_2]
for value in people:
    print(f"{value['owner']} owns a {value['animal']} and he has owned it for {value['duration']} years")