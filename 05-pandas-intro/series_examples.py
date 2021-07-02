import pandas as pd

series = pd.Series([21, 23, 56, 54])
print(series)

print(series.index)
print(series.values)
print(series.dtype)

brands = ['BMW', 'Jaguar', 'Ford', 'Kia']
quantities = [20, 10, 50, 75]
series2 = pd.Series(quantities, index=brands)
print(series2)

# Access via index
print(f'series[1]: {series[1]}')
print(f"series2['Jaguar']: {series2['Jaguar']}")
print(f"series2[['Jaguar', 'BMW', 'Kia']]: \n{series2[['Jaguar', 'BMW', 'Kia']]}")

print(series)
print('-' * 25)
print(series * 2)

print(series2.apply(lambda i: i if i > 50 else i * 2))

print(series2[series2 > 30])
