import pandas as pd

cities = {
        'name': ['London', 'Berlin', 'Madrid', 'Rome', 'Paris', 'Bristol'],
        'population': [8615246, 3562166, 3165235, 2874038, 2273305, 205544],
        'country': ['England', 'Germany', 'Spain', 'Italy', 'France', 'England']}

print('-' * 10)
city_df = pd.DataFrame(cities)
grouped_df = city_df.groupby('country')
print(grouped_df.get_group('England'))
print('-' * 10)
print(grouped_df.get_group('Spain'))
print('-' * 10)
print(grouped_df.sum())
print('-' * 10)
print(grouped_df.get_group('England').sum())
print('-' * 10)
print(grouped_df.get_group('England').agg([sum, 'mean', 'std']))
