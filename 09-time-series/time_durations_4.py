from datetime import datetime

import numpy as np
import pandas as pd

week_duration = pd.to_timedelta(np.arange(7), 'D')
print(week_duration)

print('-' * 25)

month_duration = pd.to_timedelta(np.arange(4), 'W')
print(month_duration)

print('-' * 25)

locations = ['London', 'Cardiff', 'Glasgow']
temperatures = [
        [18, 20, 21],
        [17, 19, 16],
        [17, 19, 18],
        [18, 17, 16],
        [19, 23, 19]
]
dates = [datetime(2021, 6, 1) + delta for delta in pd.to_timedelta(np.arange(5), 'D')]

df = pd.DataFrame(temperatures,
                  index=dates,
                  columns=locations)
print(df.to_string())
