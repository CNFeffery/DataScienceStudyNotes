import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(
    __name__,
    external_stylesheets=['css/bootstrap.min.css']
)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('start', width=3, style={'border': '1px solid black'}),
                    dbc.Col('start', width=3, style={'border': '1px solid black'}),
                    dbc.Col('start', width=3, style={'border': '1px solid black'})
                ],
                justify='start'
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('center', width=3, style={'border': '1px solid black'}),
                    dbc.Col('center', width=3, style={'border': '1px solid black'}),
                    dbc.Col('center', width=3, style={'border': '1px solid black'})
                ],
                justify='center'
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('end', width=3, style={'border': '1px solid black'}),
                    dbc.Col('end', width=3, style={'border': '1px solid black'}),
                    dbc.Col('end', width=3, style={'border': '1px solid black'})
                ],
                justify='end'
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('between', width=3, style={'border': '1px solid black'}),
                    dbc.Col('between', width=3, style={'border': '1px solid black'}),
                    dbc.Col('between', width=3, style={'border': '1px solid black'})
                ],
                justify='between'
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('around', width=3, style={'border': '1px solid black'}),
                    dbc.Col('around', width=3, style={'border': '1px solid black'}),
                    dbc.Col('around', width=3, style={'border': '1px solid black'})
                ],
                justify='around'
            )
        ],
        # 为Container两边添加参考线
        style={'border-left': '1px solid red', 'border-right': '1px solid red'}
    )
)

if __name__ == '__main__':
    app.run_server()