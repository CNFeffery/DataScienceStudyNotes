import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(dbc.Button('A', id='A', n_clicks=0)),
                    dbc.Col(dbc.Button('B', id='B', n_clicks=0)),
                    dbc.Col(dbc.Button('C', id='C', n_clicks=0))
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.P('按钮A未点击', id='A-output')),
                    dbc.Col(html.P('按钮B未点击', id='B-output')),
                    dbc.Col(html.P('按钮C未点击', id='C-output'))
                ]
            ),
            dbc.Row(
                dbc.Col(
                    html.Pre(id='raw-json')
                )
            )
        ]
    )
)


@app.callback(
    [Output('A-output', 'children'),
     Output('B-output', 'children'),
     Output('C-output', 'children'),
     Output('raw-json', 'children')],
    [Input('A', 'n_clicks'),
     Input('B', 'n_clicks'),
     Input('C', 'n_clicks')],
    prevent_initial_call=True
)
def refresh_output(A_n_clicks, B_n_clicks, C_n_clicks):

    # 获取本轮回调状态下的上下文信息
    ctx = dash.callback_context

    # 取出对应State、最近一次触发部件以及Input信息
    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return A_n_clicks, B_n_clicks, C_n_clicks, ctx_msg

if __name__ == '__main__':
    app.run_server(debug=True)