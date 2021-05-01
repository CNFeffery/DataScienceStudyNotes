import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.A('页面A', href='/pageA'),
                        html.Br(),
                        html.A('页面B', href='/pageB'),
                        html.Br(),
                        html.A('页面C', href='/pageC'),
                    ],
                    width=2,
                    style={
                        'backgroundColor': '#eeeeee'
                    }
                ),
                dbc.Col(
                    html.H3(id='render-page-content'),
                    width=10
                )
            ]
        )
    ],
    style={
        'paddingTop': '20px',
        'height': '100vh',
        'weight': '100vw'
    }
)


@app.callback(
    Output('render-page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return '欢迎来到首页'

    elif pathname == '/pageA':
        return '欢迎来到页面A'

    elif pathname == '/pageB':
        return '欢迎来到页面B'

    elif pathname == '/pageC':
        return '欢迎来到页面C'

    else:
        return '当前页面不存在！'


if __name__ == '__main__':
    app.run_server(debug=True)
