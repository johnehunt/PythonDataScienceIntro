import pandas as pd

df = pd.DataFrame([[57, 54, 75], [86, 54, 56]],
                   index=pd.Index(['John', 'Denise'], name='student'),
                   columns=pd.Index(['English', 'Maths', 'History'], name='subject'))
print(df.to_string())

print('-' * 25)

# Pivot the columns into rows producing a series
# aka stack the columns into a hierarchical indexed series
stacked_series = df.stack()
print(stacked_series)

print('-' * 25)

s1 = stacked_series['John']
print(s1)
print(s1.dtype)
print(s1.shape)
print(s1['English'])
for index, value in s1.iteritems():
    print(f'Index: {index} - value {value}')
s1.apply(lambda e: print(e))


print('-' * 25)

# Can unstack / rearrange hierarchically indexed series back to
# a Dataframe using unstack

df2 = stacked_series.unstack()
print(df2)

print('-' * 25)


