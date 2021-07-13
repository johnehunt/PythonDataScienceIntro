from datetime import datetime
import pandas as pd

dates = [datetime(2020, 11, 1),
         datetime(2020, 6, 2),
         datetime(2021, 6, 1),
         datetime(2021, 6, 2),
         datetime(2021, 7, 1)]
ts = pd.Series([18, 20, 21, 17, 19], index=dates)
print(ts)

print('-' * 24)

# Get all rows for a given year
print(ts['2020'])

# Get all rows for a given year and month
print(ts['2021-06'])

# Get all rows for a given month whatever the year
print(ts[ts.index.month == 6])

print('-' * 24)

print(ts['2021-06-01': '2021-07-01'])


