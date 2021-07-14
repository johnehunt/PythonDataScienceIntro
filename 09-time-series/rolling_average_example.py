import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

df = pd.read_csv('google_trends_holidays_uk.csv', skiprows=1)
df.columns = ['month', 'holiday', 'travel', 'flights']
df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
print(df.head().to_string())

print(df['holiday'])
print(df['holiday'].rolling(12))
print('-' * 25)
print(df['holiday'].rolling(12).mean())

df_means = pd.concat([df['holiday'].rolling(12).mean(),
                      df['travel'].rolling(12).mean(),
                      df['flights'].rolling(12).mean()], axis=1)

df_means.plot(figsize=(20, 10), linewidth=2, fontsize=10)
plt.xlabel('Year', fontsize=15)

plt.show()