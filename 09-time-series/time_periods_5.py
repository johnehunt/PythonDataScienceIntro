import pandas as pd

period = pd.Period('2020-06', freq='M')
print(period)
print(period.asfreq('D', 'start'))
print(period.asfreq('D', 'end'))

# Can perform period arithmetic - increment month
print(period + 1)

# Can create period range per month in a year
monthly_period_range = pd.period_range('2020-01', '2021-12', freq='M')
print(monthly_period_range)

# Creating a Period covering all years in a range
year_period_range = pd.period_range('2015', '2021', freq='A-DEC')
print(year_period_range)

# Quarterly Periods
quarterly_period = pd.Period('2020Q4', freq='Q-DEC')
print(quarterly_period)
print(quarterly_period.asfreq('D', 'start'))
print(quarterly_period.asfreq('D', 'end'))

# Using a period range with a Dataframe
dates = pd.period_range('2020-06-01', '2020-06-05', freq='D')

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
