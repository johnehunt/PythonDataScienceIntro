import pandas as pd

df1 = pd.DataFrame({'student' : ['John', 'Denise', 'John', 'Adam'],
                    'data1' : [57, 54, 75, 86]})
df2 = pd.DataFrame({'student' : ['Jasmine', 'John', 'Adam'],
                    'data2' : [72, 65, 66]})
df3 = pd.merge(df1, df2)
print(df3.to_string())

print('-' * 25)


