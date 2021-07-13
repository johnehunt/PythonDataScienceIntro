import pandas as pd

df1 = pd.DataFrame([[56, 76],
                    [75, 68],
                    [67, 64]],
                   index=['John', 'Denise', 'Adam'],
                   columns=['English', 'Maths'])
df2 = pd.DataFrame([[62, 37],
                    [75, 89]],
                   index=['John', 'Adam'],
                   columns=['Physics', 'Chemistry'])
print(df1)
print('.' * 25)
print(df2)

print('-' * 25)

combined_df = pd.concat([df1, df2], axis='columns')
print(combined_df)

print('-' * 25)

combined_df = pd.concat([df1, df2], axis='columns', keys=['semester1', 'semester2'])
print(combined_df)
