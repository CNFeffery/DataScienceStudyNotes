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
            dbc.Row(
                dbc.Col(
                    dbc.Button('按钮',
                               color='primary',
                               id='button',
                               n_clicks=0)
                )
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('尚未触发', id='record-1'),
                    dbc.Col('尚未触发', id='record-2'),
                    dbc.Col('尚未触发', id='record-n')
                ]
            )
        ]
    )
)


@app.callback(
    [Output('record-1', 'children'),
     Output('record-2', 'children'),
     Output('record-n', 'children'),
     ],
    Input('button', 'n_clicks'),
    prevent_initial_call=True
)
def record_click_event(n_clicks):
    if n_clicks == 1:
        return (
            '第1次点击：{}'.format(time.strftime('%H:%M:%S', time.localtime(time.time()))),
            dash.no_update,
            dash.no_update
        )

    elif n_clicks == 2:
        return (
            dash.no_update,
            '第2次点击：{}'.format(time.strftime('%H:%M:%S', time.localtime(time.time()))),
            dash.no_update
        )

    elif n_clicks >= 3:
        return (
            dash.no_update,
            dash.no_update,
            '第3次及以上点击：{}'.format(time.strftime('%H:%M:%S', time.localtime(time.time()))),
        )


if __name__ == '__main__':
    app.run_server(debug=True)