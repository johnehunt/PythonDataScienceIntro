import pandas as pd

df = pd.read_csv('data_set1.csv')
df.set_index('id', inplace = True)
print(df.to_string())

# Find all null values - True means value is missing
is_null_values = df.isnull()
print(is_null_values)

print('-' * 25)

# Count the number of True (missing values) for each column
is_null_count = df.isnull().sum()
print(is_null_count)

print('-' * 25)

# Number of non-NA values
print(df.count)

# Can drop a column with no useful information, for example
# axis - indicates drop a column, inplace=True means in the df not a copy
new_df = df.drop('notes', axis='columns')
print(new_df.to_string())

# Can also drop rows based on presence of missing values in that row
new_df = df.dropna(subset=['notes'])
print(new_df.to_string())

print('-' * 25)
# Drop unused columns
print(df.to_string())
df.drop('zone', axis='columns', inplace=True)
print(df.to_string())