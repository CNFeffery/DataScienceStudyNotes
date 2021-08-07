import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css']
)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='input1'),
                        width=4
                    ),
                    dbc.Col(
                        dbc.Label(id='output1'),
                        width=4
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='input2'),
                        width=4
                    ),
                    dbc.Col(
                        dbc.Label(id='output2'),
                        width=4
                    )
                ]
            )
        ]
    )
)

@app.callback(
    Output('output1', 'children'),
    Input('input1', 'value')
)
def callback1(value):

    if value:
        return int(value) ** 2


@app.callback(
    Output('output2', 'children'),
    Input('input2', 'value')
)
def callback2(value):

    if value:
        return int(value) ** 0.5

if __name__ == "__main__":
    app.run_server(debug=True)