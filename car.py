import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import dash
from dash.dependencies import Output, Input
import pandas as pd
import numpy as np

app = dash.Dash()

df = pd.read_csv('Data/mpg.csv')
df['year'] = np.random.randint(-4,5, len(df))*0.1 + df['model_year']


app.layout = html.Div([
    html.Div([
        dcc.Graph(id='car-scatter',
                  figure={'data': [go.Scatter(
                    x=df['year']+1900,
                    y=df['mpg'],
                    text=df['name'],
                    hoverinfo= 'text'+'x'+'y',
                    mode='markers',

                )], 'layout': go.Layout(
                    title='Carros Massa !',
                    xaxis={'title': 'Modelo'},
                    yaxis={'title': 'Potência'},
                    hovermode='closest'
                )})
    ],style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id='aceleracao',
                  figure={
                      'data': [go.Scatter(
                          x=[0,1],
                          y=[0,1],
                          mode='lines',
                      )],
                      'layout': go.Layout(
                        title='Aceleração',
                        margin={'l': 0}
                      )
                  })
    ], style={'width': '20%', 'height': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Markdown(id='status')
    ], style={'width': '20%', 'height': '50%', 'display': 'inline-block'})
])


@app.callback(Output('aceleracao', 'figure'),
              [Input('car-scatter', 'hoverData')])
def call_scatter(hoverData):

    v_index = hoverData['points'][0]['pointIndex']
    data = [go.Scatter(
                x=[0, 1],
                y=[0, 60/df.iloc[v_index]['acceleration']],
                mode='lines',
                line={'width': 3*df.iloc[v_index]['cylinders']}
    )]

    layout = go.Layout(title=df.iloc[v_index]['name'],
                       xaxis={'visible': True},
                       yaxis={'visible': True, 'range': [0, 60/df['acceleration'].min()]},
                       margin={'l': 0},
                       height=300)

    figure = {'data': data, 'layout': layout}

    return figure

@app.callback(Output('status', 'children'),
              [Input('car-scatter', 'hoverData')])
def call_status(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
         {} >> Cilindros   
         {} >> Cavalos      
         Faz de 0 a 60 mph em {} segundos
    """.format(df.iloc[v_index]['cylinders'], df.iloc[v_index]['horsepower'], df.iloc[v_index]['acceleration'])

    return stats

if __name__ == '__main__':
    app.run_server()