favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
people = ['jen', 'sarah', 'phil', 'john', 'samuel']
for name in people:
    print(name.title())
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"I am inviting {name.title()} to take our poll.")