import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}
#
# fig = {'data': [{'x': [1, 2, 3], 'y':[4, 1, 2], 'type':'bar', 'name':'SF'},
#                 {'x': [1, 2, 3], 'y':[2, 4, 5], 'type':'bar', 'name':'NYC'}
#                 ],
#        'layout': {'plot_bgcolor': colors['background'],
#                   'paper_bgcolor': colors['background'],
#                   'font': {'color': colors['text']},
#                   'title': 'Plotagem de Barra!'}
#        }

np.random.seed(42)
rand_x = np.random.randint(1, 101, 100)
rand_y = np.random.randint(1, 101, 100)

trace1 = go.Scatter(x=rand_x, y=rand_y, mode='markers',
                    marker={'size':12,
                              'color': 'rgb(51,204,153)',
                              'line': {'width':2}})
trace2 = go.Scatter(x=rand_x, y=rand_y, mode='markers',
                    marker={'size':12,
                              'color': 'rgb(51,254,153)',
                              'line': {'width':2}})
layout1 = go.Layout(title='Scatter 1')
layout2 = go.Layout(title='Scatter 2')


app.layout = html.Div(children=[
                        html.H1('Numeros Aleatorios', style={'textAlign': 'center',
                                                      'color': colors['text']}),
                        html.Div('Dash: Web Dashboards', style={'textAlign': 'center'}),
                        html.Div([dcc.Graph(id='scatter1', figure={'data': [trace1], 'layout': layout1},
                                    style={'backgroundColor': colors['background']}),
                                  dcc.Graph(id='scatter2', figure={'data': [trace2], 'layout': layout2},
                                    style={'backgroundColor': colors['background']})])
                        ])

if __name__ == '__main__':
        app.run_server()

