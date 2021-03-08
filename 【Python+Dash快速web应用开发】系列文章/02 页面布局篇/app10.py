import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(
            [
                dbc.Row(style={'height': '30px'}),  # 利用css设置高度
                dbc.Row(
                    dbc.Col('Email address')
                ),
                dbc.Row(
                    dbc.Col(dbc.Input(placeholder='Enter email'))
                ),
                dbc.Row(
                    dbc.Col('Password')
                ),
                dbc.Row(
                    dbc.Col(dbc.Input(placeholder='Enter Password'))
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            'By signing up you accept our ',
                            html.A('Terms Of Use', href='#')
                        ],
                        width={'size': 10, 'offset': 1},
                        style={'text-align': 'center'}  # 利用css设置文字居中
                    ),
                    style={'margin': '6px'}  # 利用css设置上下留白高度
                ),
                dbc.Row(
                    dbc.Col(
                        # 利用css实现圆角矩形效果
                        dbc.Button('LOGIN', style={'border-radius': '18px'}, block=True),
                        width={'size': 8, 'offset': 2},
                        style={'text-align': 'center'}
                    )
                ),
                dbc.Row(
                    [
                        dbc.Col(html.Hr()),
                        html.P('or', style={'text-align': 'center', 'margin': 0}),
                        dbc.Col(html.Hr())
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Button(
                            'Signup using Google',
                            style={'border-radius': '18px'},
                            block=True,
                            outline=True
                        ),
                        width={'size': 8, 'offset': 2},
                        style={'text-align': 'center'}
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        [
                            "Don't have account? ",
                            html.A('Sign up here', href='#')
                        ],
                        width={'size': 10, 'offset': 1},
                        style={'text-align': 'center'}
                    ),
                    style={'margin': '6px'}
                ),
                html.Br(),
            ],
            style={
                'background-color': '#ededef',  # 设置背景颜色
                'max-width': '480px',  # 为Container部件设置最大宽度
                'border-radius': '12px'
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server()