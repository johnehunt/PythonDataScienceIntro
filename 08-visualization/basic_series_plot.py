import pandas as pd
import numpy.random as random
import matplotlib.pyplot as pyplot

ts = pd.Series(random.randn(72), index=pd.date_range('1/1/2015', periods=72))
ts = ts.cumsum()
ts.plot()
pyplot.show()
