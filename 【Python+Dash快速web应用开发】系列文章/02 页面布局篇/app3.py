import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # fluid默认为False
        dbc.Container(
            [
                dcc.Dropdown(),
                '测试',
                dcc.Dropdown()
            ]
        ),

        html.Hr(), # 水平分割线

        # fluid设置为True
        dbc.Container(
            [
                dcc.Dropdown(),
                '测试',
                dcc.Dropdown()
            ],
            fluid=True
        )
    ]
)

if __name__ == "__main__":
    app.run_server()