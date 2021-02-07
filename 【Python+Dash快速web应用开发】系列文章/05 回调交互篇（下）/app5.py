import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Button('服务端回调', id='server-button'),
            dbc.Collapse('服务端折叠内容', id='server-collapse'),
            html.Hr(),
            dbc.Button('浏览器端回调', id='browser-button'),
            dbc.Collapse('浏览器端折叠内容', id='browser-collapse'),
        ]
    )
)


@app.callback(
    Output('server-collapse', 'is_open'),
    Input('server-button', 'n_clicks'),
    State('server-collapse', 'is_open'),
    prevent_initial_call=True
)
def server_callback(n_clicks, is_open):
    return not is_open

# 在dash中定义浏览器端回调函数的特殊格式
app.clientside_callback(
    """
    function(n_clicks, is_open) {
        return !is_open;
    }
    """,
    Output('browser-collapse', 'is_open'),
    Input('browser-button', 'n_clicks'),
    State('browser-collapse', 'is_open'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run_server(debug=True)