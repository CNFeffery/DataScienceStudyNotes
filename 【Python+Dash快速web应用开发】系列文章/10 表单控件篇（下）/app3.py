import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("https://www.cnblogs.com/", addon_type="prepend"),
                    dbc.Input(placeholder="输入博客园用户名")
                ]
            ),
            html.Br(),
            dbc.InputGroup(
                [
                    dbc.Input(placeholder="输入qq邮箱"),
                    dbc.InputGroupAddon("@qq.com", addon_type="append")
                ]
            )
        ],
        style={
            'margin-top': '200px',
            'max-width': '400px'
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)