import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

# print(iris)

# sns.scatterplot(x = iris.sepal_length, y = iris.sepal_width)

# sns.scatterplot(x = iris.sepal_length, y = iris.petal_length)

# sns.scatterplot(x = iris.petal_length, y = iris.petal_width)

# sns.displot(iris['sepal_length'])

tips = sns.load_dataset("tips")
# sns.scatterplot(x = tips.total_bill, y = tips.tip)
# print(tips['smoker'].value_counts())

# sns.relplot(x = tips.total_bill , y = tips.tip, data = tips , hue = 'smoker')
# sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,style='size')

# sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,style='size',hue='smoker')

# sns.relplot(x=tips.total_bill,y=tips.tip,data=tips,style='size',hue='time')

# sns.catplot(x='day',y='total_bill',data=tips)

# sns.catplot(x='smoker',y='tip',data=tips)

# sns.jointplot(x=tips.total_bill,y=tips.tip)

sns.pairplot(tips)

plt.show()