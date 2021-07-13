import seaborn as sns
import matplotlib.pyplot as pyplot

sns.set()

dots = sns.load_dataset("dots")
sns.relplot(x="time", y="firing_rate", col="align",
            hue="choice", size="coherence", style="choice",
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=dots)


# sns.relplot(x="time", y="firing_rate", col="align",
#             hue="choice", size="coherence", style="choice",
#             facet_kws=dict(sharex=False),
#             kind="scatter", legend="full", data=dots)

pyplot.show()
