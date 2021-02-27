import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [
                            html.Th('字段1'),
                            html.Th('字段2'),
                            html.Th('字段3'),
                            html.Th('字段4'),
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th('1'),
                                # style设置水平居中
                                html.Td('colSpan=2', colSpan=2, style={'text-align': 'center'}),
                                html.Td('test'),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th('2'),
                                html.Td('test'),
                                # style设置垂直居中
                                html.Td('rowSpan=2', rowSpan=2, style={'vertical-align': 'middle'}),
                                html.Td('test')
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th('3'),
                                html.Td('test'),
                                html.Td('test')
                            ]
                        )
                    ]
                )
            ],
            striped=True,
            bordered=True
        ),
        style={
            'margin-top': '50px'  # 设置顶部留白区域高度
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)