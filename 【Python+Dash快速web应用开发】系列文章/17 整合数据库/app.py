import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from model import MessageBoard, submit_new_message, fetch_all_message

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Div(style={'height': '20px'}),
            html.H2('Dash示例留言板'),
            dbc.Container(
                id='history-message',
                style={
                    'paddingTop': '50px',
                    'width': '70%',
                    'height': '70%',
                    'overflowY': 'auto',
                    'backgroundColor': '#fafafa'
                }
            ),
            dbc.Container(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Input(placeholder='输入昵称：', id='nickname', style={'width': '100%'}),
                            width=3,
                            style={
                                'padding': 0
                            }
                        ),
                        dbc.Col(
                            dbc.Input(placeholder='输入留言内容：', id='message', style={'width': '100%'}),
                            width=7,
                            style={
                                'padding': 0
                            }
                        ),
                        dbc.Col(
                            dbc.Button('提交', id='submit', color='primary', block=True),
                            width=2,
                            style={
                                'padding': 0
                            }
                        )
                    ]
                ),
                style={
                    'paddingTop': '10px',
                    'width': '70%',
                }
            )
        ],
        style={
            'height': '800px',
            'boxShadow': 'rgb(0 0 0 / 20%) 0px 13px 30px, rgb(255 255 255 / 80%) 0px -13px 30px',
            'borderRadius': '10px'
        }
    ),
    style={
        'paddingTop': '50px'
    }
)


@app.callback(
    Output('history-message', 'children'),
    Input('submit', 'n_clicks'),
    [State('nickname', 'value'),
     State('message', 'value')]
)
def refresh_message_board(n_clicks, nickname, message):
    if nickname and message:
        submit_new_message(nickname, message)

    return [
        html.Div(
            [
                html.Strong(record['nickname']),
                html.Span('　'),
                html.Em(record['pub_datetime'].strftime(format='%Y-%m-%d %H:%M:%S')),
                html.Br(),
                html.P(record['message_content'])
            ]
        )
        for record in fetch_all_message()
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
