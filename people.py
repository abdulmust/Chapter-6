user_0 = {'first_name': 'Abdullah', 'last_name': 'Mustapha', 'age': 17, 'city': 'Manchester'}
user_1 = {'first_name': 'David', 'last_name': 'Johnson', 'age': 56, 'city': 'Los Angeles'}
user_2 = {'first_name': 'Musa', 'last_name': 'Dembele', 'age': 30, 'city': 'Paris'}
people = [user_0, user_1, user_2]
for value in people:
    print(f"My name is {value['first_name']} and my last name is {value['last_name']}, I am {value['age']} years old and I live in {value['city']} ")