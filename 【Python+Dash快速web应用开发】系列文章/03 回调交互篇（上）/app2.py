import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css']
)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.Input(id='input-value1'), width=3),
                        dbc.Col(html.P('+'), width=1),
                        dbc.Col(dbc.Input(id='input-value2'), width=3),
                    ],
                    justify='start'
                ),
                html.Hr(),
                dbc.Label(id='output-value')
            ]
        )
    ]
)


@app.callback(
    Output('output-value', 'children'),
    Input('input-value1', 'value'),
    Input('input-value2', 'value')
)
def input_to_output(input_value1, input_value2):

    try:
        return float(input_value1) + float(input_value2)
    except:
        return '请输入合法参数！'


if __name__ == '__main__':
    app.run_server()