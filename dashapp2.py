import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from plotly import graph_objs as go
import pandas as pd


df = pd.read_csv('Data/gapminderDataFiveYear.csv')
# print(df)
opcao_ano = []
life_op = []

for ano in df['year'].unique():
    opcao_ano.append({'label': str(ano), 'value': ano})


for x in df['country'].unique():
    life_op.append({'label': str(x), 'value': x})


app = dash.Dash()

app.layout = html.Div([

    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker', options=opcao_ano, value=df['year'].min()),
    dcc.Dropdown(id='country', options=life_op, value=df['lifeExp'].min())
])

@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value'),
               Input('life', 'value')])
def update_figura(ano_selec, life_selec):

    df_filtro = df[(df['year']==ano_selec) & (df['lifeExp']==life_selec)]

    traces = []

    for conti_nome in df_filtro['continent'].unique():
        df_por_conti = df_filtro[df_filtro['continent']==conti_nome]
        traces.append(go.Scatter(
            x=df_por_conti['gdpPercap'],
            y=df_por_conti['lifeExp'],
            mode='markers',
            opacity=0.7,
            name=conti_nome
        ))
    return {'data': traces,
            'layout': go.Layout(title='Pesquisa',
                                xaxis={'title': 'Renda per Cap', 'type': 'log'},
                                yaxis={'title': 'Expectativa de vida', 'type': 'log'})}


if __name__ == '__main__':
    app.run_server()