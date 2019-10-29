import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot as po

np.random.seed(42)
rand_x = np.random.randint(1,101,100)
rand_y = np.random.randint(1,101,100)

data = [go.Scatter(x=rand_x, y=rand_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='circle-open-dot',
                       line={'width':2}
                   ))]

layout = go.Layout(title='Scatter Plot',
                   xaxis= {'title': 'Linha X'},
                   yaxis=dict(title='Linha Y'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

po(fig, filename='scatter.html')