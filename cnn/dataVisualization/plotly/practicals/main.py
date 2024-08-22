import plotly.graph_objects as go
import matplotlib.pyplot as plt

# fig = go.Figure()
# fig.add_trace(go.Scatter(x=[1,2,3,4,5],y=[6,7,8,9,10],mode='markers'))

# fig.add_trace(go.Scatter(x=[1,2,4,5,6],y=[3,4,2,4,5], mode='lines'))

# fig.add_trace(go.Bar(x=[1,2,3,4,5],y=[4,5,3,4,5]))

# x = [1,2,1,2,34,5,3,5,3,4,65,4,5,3,57,5,6,566,45,4,45,5,4,56,75,3]

# fig = go.Figure(data = [go.Histogram(x = x)])

import seaborn as sns

tips = sns.load_dataset('tips')
# fig = go.Figure(data = [go.Histogram(x = tips.total_bill)])

fig = go.Figure()
# fig.add_trace(go.Scatter(x=tips.total_bill, y=tips.tip, mode='markers'))

# fig.add_trace(go.Scatter(x=tips.total_bill,y=tips.tip,mode='markers',marker_size=10*tips['size']))

# fig.add_trace(go.Scatter3d(x=tips.total_bill,y=tips.tip,mode='markers',z=tips['size']))



# fig.add_trace(go.Scatter3d(x = [1,2,3,4,5],y=[5,6,7,8,9],mode='lines',z=[2,3,4,5,6]))

# fig.add_trace(go.Scatter3d(x=[1,2,34,5,6],y=[23,12,34,45,3],z=[12,3,45,3,4],mode='markers'))

fig.add_trace(go.Scatter3d(x=tips.total_bill,y=tips.tip,mode='lines',z=tips['size']))


fig.show()