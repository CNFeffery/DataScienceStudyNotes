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
                        dbc.Col(dbc.Input(id='input-lastname'), width=3),
                        dbc.Col(html.P('+'), width=1),
                        dbc.Col(dbc.Input(id='input-firstname'), width=3),
                    ],
                    justify='start'
                ),
                html.Hr(),
                dbc.Label(id='output1'),
                html.Br(),
                dbc.Label(id='output2')
            ]
        )
    ]
)


@app.callback(
    [Output('output1', 'children'),
     Output('output2', 'children')],
    [Input('input-lastname', 'value'),
     Input('input-firstname', 'value')]
)
def input_to_output(lastname, firstname):

    try:
        return '完整姓名：' + lastname + firstname, f'姓名长度为{len(lastname+firstname)}'
    except:
        return '等待输入...', '等待输入...'


if __name__ == '__main__':
    app.run_server()