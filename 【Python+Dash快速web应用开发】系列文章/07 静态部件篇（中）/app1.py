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
                            html.Th('第一列'),
                            html.Th('第二列'),
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Td('一行一列'),
                                html.Td('一行二列'),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Td('二行一列'),
                                html.Td('二行二列'),
                            ]
                        )
                    ]
                )
            ]
        ),
        style={
            'margin-top': '50px'  # 设置顶部留白区域高度
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)