from datetime import datetime
import pandas as pd

dates = [datetime(2021, 6, 1),
         datetime(2021, 6, 2),
         datetime(2021, 6, 3),
         datetime(2021, 6, 4),
         datetime(2021, 6, 7)]
ts = pd.Series([18, 20, 21, 17, 19], index=dates)
print(ts)

print('-' * 24)

print(ts.index)

print('-' * 24)

print(ts.index[2])

print('-' * 24)

timestamp = ts.index[2]
temperature = ts[timestamp]
print(temperature)

print(ts['20210603'])

