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
            )
        ]
    )
)


@app.callback(
    Output('output1', 'children'),
    Input('input1', 'value'),
    prevent_initial_call=True
)
def callback1(value):

    return int(value) ** 2


if __name__ == "__main__":
    app.run_server(debug=True)