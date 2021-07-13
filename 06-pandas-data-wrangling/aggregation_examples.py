import pandas as pd

df = pd.DataFrame({'day': ['2021-04-09', '2021-04-10', '2021-04-11', '2021-04-12', '2021-04-13'],
                   'sales': [101, 145, 53, 56, 76],
                   'people' : [1, 2, 2, 1, 3]})
df['day'] = pd.to_datetime(df['day'])
print(df.to_string())

print('-' * 25)

# Common aggregation
print(f'Total sales: {df["sales"].sum()}')
print(f'Mean sales: {df["sales"].mean()}')
print(f'Median sales: {df["sales"].median()}')
print(f'Min sales: {df["sales"].min()}')
print(f'Max sales: {df["sales"].max()}')
print(f'Product of sales: {df["sales"].prod()}')

print('-' * 25)

combined_results = df['sales'].agg(['mean', 'std', max, min])
print(combined_results.to_string())

print('-' * 25)

df['avg_sales_per_person'] = df['sales'] / df['people']
print(df.to_string())


