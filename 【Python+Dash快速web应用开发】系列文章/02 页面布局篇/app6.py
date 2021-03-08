import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Br(),  # 换行
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Container(
            [
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('1.请选择你的年龄段')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "18岁以下", "value": 1},
                                    {"label": "18到28岁", "value": 2},
                                    {"label": "28岁及以上", "value": 3}
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('2.请选择你所在的城市级别')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.RadioItems(
                                options=[
                                    {"label": "一线城市", "value": 1},
                                    {"label": "新一线城市", "value": 2},
                                    {"label": "二线城市", "value": 3},
                                    {"label": "三线城市", "value": 4},
                                    {"label": "四线城市及以下", "value": 5},
                                ],
                                inline=True
                            )
                        )
                    ]
                ),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([dbc.Label('3.请选择你所关注的城市病问题（可多选）')])
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Checklist(
                                options=[
                                    {"label": "交通拥堵", "value": 1},
                                    {"label": "空气污染", "value": 2},
                                    {"label": "公共健康", "value": 3},
                                    {"label": "用水安全", "value": 4},
                                    {"label": "其他", "value": 5}
                                ],
                                inline=True
                            ),
                        )
                    ]
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Input(type="text"),
                                    dbc.FormText("输入你的电话号码"),
                                ]
                            ),
                            width=5
                        ),
                        dbc.Col(
                            dbc.FormGroup(
                                [
                                    dbc.Input(type="text"),
                                    dbc.FormText("输入你的邮箱地址"),
                                ]
                            ),
                            width=5
                        ),
                        dbc.Col(
                            dbc.Button('提交'),
                            width=2
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server()