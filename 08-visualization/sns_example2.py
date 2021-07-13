import seaborn as sns
import matplotlib.pyplot as pyplot

sns.set()

# Tips is in-built dataset
tips = sns.load_dataset("tips")

sns.catplot(x="day",
            y="total_bill",
            hue="smoker",
            kind="swarm",
            data=tips)

pyplot.show()
