import numpy as np
import pandas as pd

cities = {
        'name': ['London', 'Berlin', 'Madrid', 'Rome', 'Paris'],
        'population': [8615246, 3562166, 3165235, 2874038, 2273305],
        'country': ['England', 'Germany', 'Spain', 'Italy', 'France']}

city_df = pd.DataFrame(cities)

print(city_df)

print(city_df.shape)

print(city_df.dtypes)
print(city_df['name'].dtype)

city_df['name'] = city_df.name.astype('string')
print(city_df['name'].dtype)
print('-' * 10)

print(city_df.head(4))
print('-' * 10)
print(city_df.tail(4))
print('-' * 10)
print(city_df.sample(4))

print('-' * 10)

df1 = pd.DataFrame(cities,
                   columns=['name', 'population'],
                   index=cities['country'])
print(df1)

print('-' * 10)

df2 = pd.DataFrame(cities)
df2.set_index('country', inplace=True)
print(df2)

df = pd.DataFrame(cities,
                  columns=('name', 'population'),
                  index=cities['country'])

new_col = df['population'].cumsum()
df['c_population'] = new_col
print(df)

sorted_frame = df.sort_values(by='population')
print(sorted_frame)

# Slicing

cities = {
        'name': ['London', 'Berlin', 'Madrid', 'Rome', 'Paris', 'Bristol'],
        'population': [8615246, 3562166, 3165235, 2874038, 2273305, 205544],
        'country': ['England', 'Germany', 'Spain', 'Italy', 'France', 'England']}

df = pd.DataFrame(cities,
                  columns=('name', 'population'),
                  index=cities['country'])

print(df.loc['England'])

print(df.loc[['England', 'Spain']])

print('-' * 10)
# Obtaining basic stats

df = pd.DataFrame([[1.4, np.nan],
                   [7.1, -1.1],
                   [1.2, 3.4],
                   [0.75, 1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print(f'df.describe(): {df.describe()}')
print(f'df.mean(): {df.mean()}')
print(f"df.mean(axis='columns'): {df.mean(axis='columns')}")
print(f"df.idxmax(): {df.idxmax()}")



print('-' * 10)
printable_frame = city_df.to_string()
print(printable_frame)

print('-' * 25)
for row_as_tuple in city_df.itertuples():
    print(row_as_tuple)

print('-' * 25)
city_df.apply(lambda x: print(x))
