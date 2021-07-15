import pandas as pd

df = pd.DataFrame({'basket_id': [0, 1, 2, 3, 4],
                   'fruit': ['apple', 'orange', 'apple', 'apple', 'orange'],
                   'count': [5, 3, 4, 2, 4]},
                  columns=['basket_id', 'fruit', 'count'])
print(df.to_string())
print(df.dtypes)

print('-' * 25)

fruit_cat = df['fruit'].astype('category')
print(fruit_cat)
print(type(fruit_cat.values))

print('-' * 25)

print(fruit_cat.values.categories)
print(fruit_cat.values.codes)

print('-' * 25)

df['fruit'] = df['fruit'].astype('category')
print(df.to_string())
print(df.dtypes)