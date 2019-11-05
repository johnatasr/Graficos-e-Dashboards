from dash.dependencies import Input,Output
import dash_html_components as html
import dash_core_components as dcc
import dash

app = dash.Dash()

app.layout = html.Div([
    dcc.RangeSlider(
        id='slider',
        max=10,
        min=-11,
        marks={i: str(i) for i in range(-11, 10)},
        value=[-1,1],
    ),
    html.H1(id='result')
])

@app.callback(Output('result', 'children'),
              [Input('slider', 'value')])
def atualiza_resultado(value):
        return value[0] * value[1]

if __name__ ==  '__main__':
    app.run_server()