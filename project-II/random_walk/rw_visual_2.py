import plotly.express as px
from plotly.graph_objs import Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values
fig = px.scatter(x_values, y_values, color=range(1, rw.num_points+1), color_continuous_scale='Reds')
fig.update_traces(marker=dict(size=5, line=dict(width=0)), selector=dict(mode='markers'))
x_axis_config = {'title': 'Steps'}
y_axis_config = {'title': 'Distance Traveled'}
my_layout = Layout(title='Random Walk Simulation of 50000 steps',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': fig, 'layout': my_layout}, filename='random_walk.html')