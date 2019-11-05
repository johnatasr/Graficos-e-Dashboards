from dash.dependencies import Input,Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import dash
import pandas as pd
import json
import base64

def codi_image(imagem):
    codimag = base64.b64encode(open(imagem, 'rb').read())
    return 'data:imagem/png;base64, {}'.format(codimag.decode())


app = dash.Dash()

df = pd.read_csv('Data/wheels.csv')


data = go.Scatter(
    x=df['color'],
    y=df['wheels'],
    dy=1,
    mode='markers',
    marker={'size': 12}
)

layout = go.Layout(title='Teste Json Retorno', hovermode='closest')

figure = {'data': [data], 'layout': layout}


app.layout = html.Div([
    html.Div([
       dcc.Graph(id='wheel-image', figure=figure, style={'width':'30%', 'float': 'left'})
    ]),
    # html.Div(
    #     html.Pre(id='hover-image', style={'paddingTop':35}), style={'width':'30%'}),
    html.Div(
        html.Img(id='img', src='children')
    )
])

@app.callback(Output('img', 'src'),
            [Input('wheel-image', 'hoverData')])
def callback_json(hoverData):

    wheel = hoverData['points']['0']['y']
    color = hoverData['points']['0']['x']
    path = 'Data/images'
    filter = path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0]

    return codi_image(filter)
    # return json.dumps(hoverData, indent=2)

if __name__== '__main__':
    app.run_server()