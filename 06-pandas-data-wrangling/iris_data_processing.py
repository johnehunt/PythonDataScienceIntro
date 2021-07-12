import pandas as pd

iris_df = pd.read_csv('iris.csv')

print(iris_df.head())
print(iris_df.shape)

print('-' * 25)

# find out information about unique values in the sample
print(iris_df.sepallength.unique())  # give the unique values
print(iris_df.sepallength.nunique())  # count the unique values

print('-' * 25)
# Dealing with duplicate values
print(iris_df.duplicated())

# Can drop all duplicate rows
iris_df.drop_duplicates(keep="first", inplace=True)
print(iris_df.duplicated())

print('-' * 25)

# Find NA down a row
print(iris_df['petallength'].isna().sum())
# FOr all columns
print(iris_df.isna().sum())
# For the whole dataset
print(iris_df.isna().sum().sum())

# Across a row
print(iris_df.loc[[1]].isna().sum().sum())