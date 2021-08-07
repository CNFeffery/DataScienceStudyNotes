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
                            html.Th('字段2')
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th('1'),
                                html.Td('test')
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th('2'),
                                html.Td('test')
                            ]
                        ),
                        html.Tr(
                            [
                                html.Td('3'),
                                html.Td('test')
                            ]
                        )
                    ]
                )
            ],
            striped=True
        ),
        style={
            'margin-top': '50px'  # 设置顶部留白区域高度
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)