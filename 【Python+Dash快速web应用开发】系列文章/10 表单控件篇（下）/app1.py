import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("用户名", html_for="username"),
                        dbc.Input(id="username", placeholder="请输入用户名", autoComplete='off')
                    ]
                ),

                dbc.FormGroup(
                    [
                        dbc.Label("账号密码", html_for="password"),
                        dbc.Input(
                            type="password",
                            id="password",
                            placeholder="请输入密码",
                        ),
                        dbc.FormText(
                            "密码必须同时包含大写字母、小写字母和数字！", color="secondary"
                        ),
                    ]
                ),

                dbc.FormGroup(
                    [
                        dbc.Button('注　册')
                    ]
                )
            ]
        ),
        style={
            'margin-top': '200px',
            'max-width': '400px'
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)