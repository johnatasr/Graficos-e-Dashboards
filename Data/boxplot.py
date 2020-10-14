import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv')

a = np.random.choice(df['rings'],100)
b = np.random.choice(df['rings'],30)

data = [go.Box(y=a, name='A'),
        go.Box(y=b, name='B')]

layout = go.Layout(title='2 Números Aleatorios')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)