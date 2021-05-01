import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dcc.Location(id='url'),
        html.Ul(id='output-url')
    ],
    style={
        'paddingTop': '100px'
    }
)


@app.callback(
    Output('output-url', 'children'),
    [Input('url', 'href'),
     Input('url', 'pathname'),
     Input('url', 'search'),
     Input('url', 'hash')]
)
def show_location(href, pathname, search, hash):
    return (
        html.Li(f'当前href为：{href}'),
        html.Li(f'当前pathname为：{pathname}'),
        html.Li(f'当前search为：{search}'),
        html.Li(f'当前hash为：{hash}'),
    )


if __name__ == '__main__':
    app.run_server(debug=True)
