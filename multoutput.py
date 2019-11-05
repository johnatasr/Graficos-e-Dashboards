from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash
import pandas as pd
import base64

df = pd.read_csv('Data/wheels.csv')

def codi_image(imagem):
    codimag = base64.b64encode(open(imagem, 'rb').read())
    return 'data:imagem/png;base64, {}'.format(codimag.decode())

app = dash.Dash()

app.layout = html.Div([

            dcc.RadioItems(
                id='wheels',
                options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                value=1,
            ),
            html.Div(id='wheels-output'),
            html.Hr(),
            dcc.RadioItems(
                id='colors',
                options=[{'label': i, 'value': i} for i in df['color'].unique()],
                value='blue',
            ),
            html.Div(id='colors-output'),
            html.Img(id='display-imagem', src='children', height=300),
            html.Hr(),
            html.Div(id='out'),
            dcc.Input(id='in', value=0, style={'fontSize': 24}),
            html.Button(id='sub-b', n_clicks=0, children='Clique'),

], style={'fontFamily': 'Helvetica', 'fontSize': 18})


@app.callback(Output('wheels-output', 'children'),
              [Input('wheels', 'value')])
def callback_wheel(wheels):
    return "Voce escolheu {} ".format(wheels)

@app.callback(Output('colors-output', 'children'),
              [Input('colors', 'value')])
def callback_color(colors):
    return "Voce escolheu {}".format(colors)

@app.callback(Output('display-imagem', 'src'),
              [Input('wheels', 'value'),
               Input('colors', 'value')])
def callback_imagem(wheel, color):
    path = 'Data/Images/'
    filter = path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0]

    return codi_image(filter)

@app.callback(Output('out', 'children'),
              [Input('sub-b', 'n_clicks')],
              [State('in', 'value')])
def printer(click, text):
    return ' Voce digitou por ultimo {} e clicou ao todo {} vezes'.format(text, click)

if __name__ == '__main__':
    app.run_server()