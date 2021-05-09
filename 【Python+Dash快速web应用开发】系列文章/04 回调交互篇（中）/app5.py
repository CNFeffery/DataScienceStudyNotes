import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css'],
    # suppress_callback_exceptions=True
)

app.layout = html.Div(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Input(id='input_num')
                    ),
                    dbc.Col(id='output_item')
                ]
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Label(id='output_desc')
                )
            )
        ]
    )
)


@app.callback(
    Output('output_item', 'children'),
    Input('input_num', 'value'),
    prevent_initial_call=True
)
def callback1(value):
    try:

        return dcc.Dropdown(
            id='output_dropdown',
            options=[
                {'label': i, 'value': i}
                for i in range(int(value))
            ]
        )
    except ValueError:
        return dash.no_update


@app.callback(
    Output('output_desc', 'children'),
    Input('output_dropdown', 'options'),
    prevent_initial_call=True
)
def callback2(options):
    return '生成的Dropdown部件共有{}个选项'.format(options.__len__())


if __name__ == "__main__":
    app.run_server(debug=True)
