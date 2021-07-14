import pandas as pd

df = pd.read_csv('icecream_v_hot_choclate.csv', skiprows=1)
df.columns = ['week', 'ice_cream', 'hot_chocolate']
df.week = pd.to_datetime(df.week)
df.set_index('week', inplace=True)
print(df.head().to_string())

print(df.corr())

