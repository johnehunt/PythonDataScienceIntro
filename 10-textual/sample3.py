from collections import Counter

import pandas as pd

cars = {'Brand': ['Ford', 'BMW', 'Ford', 'Audi', 'Ford'],
        'Model': ['Mondeo', '318', 'Fiesta', 'A4', 'Focus']}

df = pd.DataFrame(cars, columns=['Brand', 'Model'])
print(df.to_string)

print(Counter(df['Brand']).most_common())

print('-' * 25)

df_fords = df[df['Brand'] == 'Ford']
print(df_fords.to_string())
