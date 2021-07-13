import pandas as pd

cities = {
        'name': ['London', 'Berlin', 'Madrid', 'Rome', 'Paris'],
        'population': [8615246, 3562166, 3165235, 2874038, 2273305],
        'country': ['England', 'Germany', 'Spain', 'Italy', 'France']}

city_df = pd.DataFrame(cities)

print('-' * 10)
city_df = pd.DataFrame(cities)
print(city_df.sum())

print('-' * 10)
print(city_df['population'].sum())

print('-' * 10)
print(city_df['population'].cumsum())
