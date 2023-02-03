city_0 = {'city': 'paris', 'country': 'france', 'population': 'two million', 'fact': 'it has an underground city'}
city_1 = {'city': 'madrid', 'country': 'spain', 'population': 'three million', 'fact': 'Madrid means "place of abundant water'}
city_2 = {'city': 'london', 'country': 'england', 'population': 'nine million', 'fact': 'the London Underground could have been water-based'}
cities = [city_0, city_1, city_2]
for value in cities:
    print(f"{value['city'].title()} is the capital of {value['country']} and it has a population of {value['population']}, also a fact about the city is that {value['fact']}.")