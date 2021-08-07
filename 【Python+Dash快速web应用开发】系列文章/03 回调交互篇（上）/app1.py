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
                        dbc.Col(dbc.Input(id='input-value',
                                          placeholder='请输入些东西'),
                                width=12),
                        dbc.Col(dbc.Label(id='output-value'),
                                width=12)
                    ]
                )
            ]
        )
    ]
)


# 对应app实例的回调函数装饰器
@app.callback(
    Output('output-value', 'children'),
    Input('input-value', 'value')
)
def input_to_output(input_value):
    '''
    简单的回调函数
    '''
    return input_value


if __name__ == '__main__':
    app.run_server()