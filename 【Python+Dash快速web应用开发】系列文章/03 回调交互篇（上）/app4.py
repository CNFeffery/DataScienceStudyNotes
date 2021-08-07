import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

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
                        dbc.Col(dbc.Input(id='input-value'),
                                width=4),
                        dbc.Col(dbc.Button('小写转大写',
                                           id='state-button',
                                           n_clicks=0),
                                width=4),
                        dbc.Col(dbc.Label(id='output-value',
                                          style={'padding': '0',
                                                 'margin': '0',
                                                  'line-height': '38px'}),
                                width=4)
                    ],
                    justify='start'
                )
            ]
        )
    ]
)


@app.callback(
    Output('output-value', 'children'),
    Input('state-button', 'n_clicks'),
    State('input-value', 'value')

)
def input_to_output(n_clicks, value):

    if n_clicks:
        return value.upper()


if __name__ == '__main__':
    app.run_server()