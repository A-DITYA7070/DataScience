Q1. What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
    Matplotlib.
ans:- 
    Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is a widely-used library in data science, machine learning, and scientific computing, providing a flexible framework for creating a variety of plots and charts. Matplotlib is particularly known for its ability to produce publication-quality figures in various formats and interactive environments across platforms.

    Why is Matplotlib Used?
    Data Visualization: Matplotlib is used to visualize data, which helps in understanding trends, patterns, and correlations within the data.
    Flexibility: It offers extensive customization options, allowing users to create complex and aesthetically pleasing visualizations.
    Integration: It integrates well with other libraries like NumPy, Pandas, and SciPy, making it a powerful tool for data analysis.
    Publication Quality: It can produce high-quality plots that are suitable for publication in scientific journals.
    Interactivity: Matplotlib supports interactive plots that allow for real-time updates, zooming, and panning, which is useful for exploratory data analysis.
    Five Plots that Can Be Plotted Using the Pyplot Module of Matplotlib
    1. Line Plot
    2. Bar plot
    3. Scatter plot
    4. Histogram
    5. Pie chart

Q2. What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
    plot a scatter plot.
    import matplotlib.plotly as plt
    import numpy as np
    np.random.seed(3)
    x = 3 + np.random.normal(0, 2, 50)
    y = 3 + np.random.normal(0, 2, len(x))
    Note: Also add title, xlabel, and ylabel to the plot.
ans:- to add title,xlable and ylable
      plt.scatter(x,y)
      plt.xlable("x-axis")
      plt.ylable("y-axis")
      plt.title("scatter plot")
      plt.show()

Q3. Why is the subplot() function used? Draw four line plots using the subplot() function.
    Use the following data:
    import numpy as np
    For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
    For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
    For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
    For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])
ans:- 
    The subplot() function in Matplotlib is used to create a grid of plots within a single figure. 
    This is useful for comparing multiple plots side-by-side or in a structured layout. It allows
    you to organize multiple plots in rows and columns within the same figure, making it easier 
    to visualize relationships between different datasets.
    
    code:- 
    
            x1 = np.array([0, 1, 2, 3, 4, 5])
            y1 = np.array([0, 100, 200, 300, 400, 500])

            x2 = np.array([0, 1, 2, 3, 4, 5])
            y2 = np.array([50, 20, 40, 20, 60, 70])

            x3 = np.array([0, 1, 2, 3, 4, 5])
            y3 = np.array([10, 20, 30, 40, 50, 60])

            x4 = np.array([0, 1, 2, 3, 4, 5])
            y4 = np.array([200, 350, 250, 550, 450, 150])

            fig, axs = plt.subplots(2, 2, figsize=(10, 8))

            axs[0, 0].plot(x1, y1, label='Line 1')
            axs[0, 0].set_title('Plot 1')
            axs[0, 0].legend()
            axs[0, 1].plot(x2, y2, label='Line 2')
            axs[0, 1].set_title('Plot 2')
            axs[0, 1].legend()
            axs[1, 0].plot(x3, y3, label='Line 3')
            axs[1, 0].set_title('Plot 3')
            axs[1, 0].legend()
            axs[1, 1].plot(x4, y4, label='Line 4')
            axs[1, 1].set_title('Plot 4')
            axs[1, 1].legend()
            plt.tight_layout()
            plt.show()

Q4. What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
    import numpy as np
    company = np.array(["Apple", "Microsoft", "Google", "AMD"])
    profit = np.array([3000, 8000, 1000, 10000])

ans:- A bar plot (or bar chart) is a type of chart that presents categorical data with rectangular bars. 
      The lengths or heights of the bars are proportional to the values they represent. Bar plots are commonly
      used to compare the quantities of different categories.

        Bar plots are used for:

        i) Comparison: Comparing the values of different categories or groups.
        ii) Visualization: Visualizing the distribution and frequency of categorical data.
        iii) Clarity: Providing a clear and straightforward representation of data, making it easier to interpret.


Q5. What is a box plot? Why is it used? Using the following data plot a box plot.
    box1 = np.random.normal(100, 10, 200)
    box2 = np.random.normal(90, 20, 200)
ans:- 
      A bar plot (or bar chart) is a type of chart that presents categorical data with rectangular bars. 
      The lengths or heights of the bars are proportional to the values they represent. Bar plots are commonly
      used to compare the quantities of different categories.

        Bar plots are used for:

        i) Comparison: Comparing the values of different categories or groups.
        ii) Visualization: Visualizing the distribution and frequency of categorical data.
        iii) Clarity: Providing a clear and straightforward representation of data, making it easier to interpret.
