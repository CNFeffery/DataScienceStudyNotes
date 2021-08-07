import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import time

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(dbc.Spinner(color='grey')),
            dbc.Row(dbc.Spinner(color='red', type='grow')),
            dbc.Row(dbc.Button('点击计算', id='start')),
            dbc.Row(dbc.Spinner(html.P('计算结果', id='output'))),
            dbc.Row(dbc.Button('全屏点击计算', id='start-fullscreen')),
            dbc.Row(dbc.Spinner(html.P('计算结果', id='output-fullscreen'), fullscreen=True)),
        ]
    )
)

@app.callback(
    Output('output', 'children'),
    Input('start', 'n_clicks'),
    prevent_initial_call=True
)
def loading(n_clicks):

    time.sleep(1)

    return '计算完成！'

@app.callback(
    Output('output-fullscreen', 'children'),
    Input('start-fullscreen', 'n_clicks'),
    prevent_initial_call=True
)
def loading(n_clicks):

    time.sleep(1)

    return '计算完成！'

if __name__ == '__main__':
    app.run_server(debug=True)