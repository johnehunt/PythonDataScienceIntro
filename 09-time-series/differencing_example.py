import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

df = pd.read_csv('google_trends_holidays_uk.csv', skiprows=1)
df.columns = ['month', 'holiday', 'travel', 'flights']
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
print(df.head().to_string())

# df['holiday'].plot(figsize=(20,10), linewidth=2, fontsize=10)
# plt.xlabel('Year', fontsize=15)
# plt.show()

df['holiday'].diff().plot(figsize=(20,10), linewidth=2, fontsize=10)
plt.xlabel('Year', fontsize=15)
plt.show()

