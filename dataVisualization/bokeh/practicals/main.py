from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()

# output_file('test.html')

# p = figure(title="Test Flower")
# p.xaxis.axis_label = "Petal Length"
# p.yaxis.axis_label = "Petal Width"

# p.circle(flowers['petal_length'], flowers['petal_width'])
# print(flowers)

# output_file("line.html")

# p = figure(title="line graph")
# p.xaxis.axis_label = "x-axis"
# p.yaxis.axis_label = "y-axis"
# p.line(flowers['petal_length'],flowers['petal_width'])

x = [1,23,34,23,34]
y = [23,12,34,5,76]

# output_file("line_plot.html")

# p = figure(title = "line plot")
# p.line(x,y)

output_file("scatter_plot.html")
p=figure(title = "scatter plot")
p.scatter(x,y,fill_color='red',legend_label = 'red points',size=20)

show(p)
