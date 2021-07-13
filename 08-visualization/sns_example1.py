import pandas as pd
import numpy.random as random
import matplotlib.pyplot as pyplot

import seaborn as sns
sns.set()

df = pd.DataFrame(random.randn(1000, 4), columns=list(['A', 'B', 'C', 'D']))
df = df.cumsum()
df.plot()

pyplot.show()
