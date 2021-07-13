import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd

credit_score = np.random.normal(160, 6, size=100)
age = (credit_score - 100) * np.random.uniform(0.75, 1.25, 100)

gym = pd.DataFrame({'credit_score': credit_score, 'age': age})

gym.plot.scatter(x='age', y='credit_score')

pyplot.show()
