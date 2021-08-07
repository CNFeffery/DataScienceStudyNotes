import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dcc.Location(id='url'),

        dcc.Link('页面A', href='/pageA', refresh=True),
        html.Br(),
        dcc.Link('页面B', href='/pageB'),

        html.Hr(),

        html.H1(id='render-page-content')
    ],
    style={
        'paddingTop': '100px'
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
