favorite_numbers = {'sam': [2, 0], 'tolu': [9, 1], 'john': [5, 4], 'daniel': [7, 8], 'obi': [3, 6]}
for name, numbers in favorite_numbers.items():
    for number in numbers:
        print(f"{name.title()}'s favorite numbers are {number}")