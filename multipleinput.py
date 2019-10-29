from dash.dependencies import Input,Output
import dash_html_components as html
import dash_core_components as dcc
from plotly.graph_objs import  graph_objs as go
import dash
import pandas as pd

df = pd.read_csv('Data/mpg.csv')

app = dash.Dash()

colunas = df.columns

app.layout = html.Div([
            html.Div([
                dcc.Dropdown(id='xaxis',
                             options=[{'label': i, 'value': i} for i in colunas],
                             value= 'displacement'
                             )], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(id='yaxis',
                             options=[{'label': i, 'value': i} for i in colunas],
                             value='mpg')],
                            style={'width': '48%', 'display': 'inline-block'}),
            dcc.Graph(id='displace_graph')
           ], style={'padding': '10'})

@app.callback(Output('displace_graph', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):

    trace = go.Scatter(x=xaxis_name,
                       y=yaxis_name,
                       text=df['name'],
                       mode='markers',
                       markers={'size': 15,
                                'opacity': 0.5,
                                'line':{'width': 0.5, 'color': 'white'}
                                })
    layout = go.Layout(title='Carros',
                       xaxis={'title':xaxis_name},
                       yaxis={'tilte':yaxis_name},)

    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    app.run_server()