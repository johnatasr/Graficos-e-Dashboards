import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot as po

np.random.seed(56)
rand_x = np.linspace(0,1,100)
rand_y = np.random.randn(100)

trace0 = go.Scatter(x=rand_x, y=rand_y+5, mode='markers', name='marcadores')

trace1 = go.Scatter(x=rand_x, y=rand_y+10, mode='lines', name='linhas')

trace2 = go.Scatter(x=rand_x, y=rand_y, mode='lines', name='jogodoido')


data = [trace0, trace1, trace2]

layout = go.Layout(title='Lines Plot',
                   xaxis= {'title': 'Linha X'},
                   yaxis=dict(title='Linha Y'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

po(fig, filename='scatter.html')