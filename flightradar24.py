import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash

app = dash.Dash()

app.layout = html.Div([
                html.Div([
                    html.Iframe(src="https://www.flightradar24.com", height=500, width=500)
                ])
                html.Div([
                    html.Pre(id='contador_text',
                             children='Rodas ativas no mundo'),
                    dcc.Interval(id='int_component',
                                 interval=6000,
                                 n_intervals=0)
                ])
])

app.callback(Ou)

def update_layout(n):