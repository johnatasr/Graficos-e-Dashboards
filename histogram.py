import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv('Data/abalone.csv')

data = [go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))]

layout = go.Layout(title='Car Histogram')

fig = go.Figute(data=data, layout=layout)

pyo.plot(fig)