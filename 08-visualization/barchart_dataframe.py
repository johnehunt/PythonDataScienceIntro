import matplotlib.pyplot as pyplot
import pandas as pd

df = pd.DataFrame({'modules': ['CS101', 'CS105', 'CS121'], 'average_marks': [55, 63, 57]})
df.plot.bar(x='modules', y='average_marks', rot=0)

pyplot.show()
