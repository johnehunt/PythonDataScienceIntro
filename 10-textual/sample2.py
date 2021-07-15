import pandas as pd

s4 = pd.Series([1, 2, 5], dtype="Int64")
print(s4.dtypes)
print(s4)

s5 = s4.astype("string")
print(s5.dtypes)
print(s5)

print('-' * 25)

cars = {'Brand': ['Jaguar', 'BMW', None, 'Audi'],
        'Price': [56000, 39000, None, 36000]}

df = pd.DataFrame(cars, columns=['Brand', 'Price'])
print(df.to_string)

df['Brand'] = df.Brand.astype('string')
print(df.to_string)

print('-' * 25)

brands = df['Brand']
print(brands.str.match('BMW'))

print('-' * 25)

print(brands.str.len())
print(brands.str.cat(sep=';'))
print(brands.str.cat(['F Type', 'X1', None, 'A4']))
print(brands.str[0])
pattern = r'Jag'
print(brands.str.contains(pattern))


