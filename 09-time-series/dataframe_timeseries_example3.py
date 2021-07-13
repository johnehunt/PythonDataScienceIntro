from datetime import datetime
import pandas as pd

dates = [datetime(2020, 11, 1),
         datetime(2020, 6, 2),
         datetime(2021, 6, 1),
         datetime(2021, 6, 2),
         datetime(2021, 7, 1)]

locations = ['London', 'Cardiff', 'Glasgow']
temperatures = [
        [18, 20, 21],
        [17, 19, 16],
        [17, 19, 18],
        [18, 17, 16],
        [19, 23, 19]
]

df = pd.DataFrame(temperatures,
                  index=dates,
                  columns=locations)
print(df.to_string())

timestamp = df.index[1]
print(timestamp)

print(df.loc[datetime(2021, 6, 2)])
print(df.loc['2021-06'])
print(df.loc['2021'])


