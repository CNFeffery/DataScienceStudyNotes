import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡1')
                    ],
                    label='选项卡1'
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡2')
                    ],
                    label='选项卡2'
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        html.P('这是选项卡3')
                    ],
                    label='选项卡3',
                    tab_style={'margin-left': 'auto'}
                ),
            ]
        ),
        style={'margin-top': '100px'}
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)