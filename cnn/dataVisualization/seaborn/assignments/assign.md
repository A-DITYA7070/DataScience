Q1. Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.
ans:- 
    Scatter Plot (sns.scatterplot)
    Use: Scatter plots are used to visualize the relationship between two continuous variables. Each point represents an observation in the dataset.
    Example Use Case: Plotting the relationship between height and weight to see if there is a correlation.

    Histogram (sns.histplot)
    Use: Histograms display the distribution of a single continuous variable by dividing the data into bins and counting the number of observations in each bin.
    Example Use Case: Showing the distribution of ages in a population.

    Box Plot (sns.boxplot):- 
    Use: Box plots (or box-and-whisker plots) provide a summary of the distribution of a dataset, showing the median, quartiles, and potential outliers.
    Example Use Case: Comparing the distribution of test scores across different classes.

    Heatmap (sns.heatmap)
    Use: Heatmaps visualize matrix-like data, where individual values are represented by color. They are particularly useful for displaying correlation matrices or for visualizing missing data.
    Example Use Case: Showing the correlation matrix of multiple financial indicators to identify relationships between them.

    Pair Plot (sns.pairplot):- 
    Use: Pair plots visualize the pairwise relationships in a dataset. It creates a matrix of scatter plots for each pair of variables and can include histograms or KDE plots along the diagonal.
    Example Use Case: Exploring relationships between several features in a dataset to identify patterns and potential multicollinearity.

Q2. Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
    "timepoint" and y = "signal" for different events and regions.
ans:- 
        import seaborn as sns
        import matplotlib.pyplot as plt
        fmri = sns.load_dataset("fmri")
        sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", style="region")
        plt.show()

Q3. Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
    'pclass', y = 'age' and y = 'fare'.
ans:- 
     import seaborn as sns
     import matplotlib.pyplot as plt
     titanic = sns.load_dataset("titanic")
     sns.boxplot(data=titanic, x="pclass", y="age")
     plt.show()

Q4. Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
    parameter for the 'cut' column of the diamonds dataset.
ans:- 
     import seaborn as sns
     import matplotlib.pyplot as plt
     diamonds = sns.load_dataset("diamonds")
     sns.histplot(data=diamonds, x="price", hue="cut")
     plt.show()

Q5. Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
    of the iris dataset.
ans:- 
      import seaborn as sns
      import matplotlib.pyplot as plt
      iris = sns.load_dataset("iris")
      sns.pairplot(data=iris, hue="species")
      plt.show()

Q6. Use the "flights" dataset from seaborn to plot a heatmap.
ans:- 
     import seaborn as sns
     import matplotlib.pyplot as plt
     flights = sns.load_dataset("flights")
     flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
     sns.heatmap(data=flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
     plt.show()