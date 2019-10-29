import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('Data/mpg.csv')
# print(df)
data= [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

# data = [go.Scatter(x=df['displacement'],
#                     y=df['acceleration'],
#                     text=df['name'],
#                     mode='markers',
#                     marker=dict(size=df['weight']/400,))]


layout = go.Layout(title='Carros', hovermode='closest')

fig = go.Figure(data=data, layout=layout)


pyo.subplot(fig)