import seaborn as sns
import matplotlib.pyplot as plt

# fmri = sns.load_dataset('fmri')
# sns.lineplot(x="timepoint",y="signal",data=fmri,style="region",hue="event")
# plt.show()


# titanic = sns.load_dataset("titanic")
# sns.boxplot(data=titanic, x="pclass", y="age")
# plt.show()


# diamonds = sns.load_dataset("diamonds")
# sns.histplot(data=diamonds, x="price", hue="cut")

# iris = sns.load_dataset("iris")
# sns.pairplot(data=iris, hue="species")

flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(data=flights_pivot, annot=True, fmt="d", cmap="YlGnBu")


plt.show()