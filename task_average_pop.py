city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

total_population = 0
for item in city_list:
    total_population += item["population"]

num_cities = len(city_list)  # TODO найдите количество городов в списке

print(f"Среднее арифметическое населения равно = {total_population / num_cities}")
# TODO распечатайте среднее арифметическое населения
