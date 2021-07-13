import pandas as pd
import numpy.random as random
import matplotlib.pyplot as pyplot

df = pd.DataFrame(random.randn(1000, 4), columns=list(['A', 'B', 'C', 'D']))
df = df.cumsum()

pyplot.figure()
df.plot()

pyplot.show()
