import pandas as pd

s1 = pd.Series(['a', 'b', 'c'])
print(s1.to_string())
print(s1.dtypes)

s2 = pd.Series(["a", "b", "c"], dtype='string')
print(s2.to_string())
print(s2.dtypes)

s3 = pd.Series(['a', 'b', "c"], dtype=pd.StringDtype())
print(s3.to_string())
print(s3.dtypes)
