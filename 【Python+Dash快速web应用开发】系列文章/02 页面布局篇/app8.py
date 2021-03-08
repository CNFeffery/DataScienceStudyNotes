import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('1', width=2, style={'background-color': 'lightblue'}),
                    dbc.Col('2', width=2, style={'background-color': 'lightskyblue'}),
                    dbc.Col('3', width=2, style={'background-color': '#e88b00'}),
                    dbc.Col('4', width=2, style={'background-color': '#8c8c8c'})
                ],
                style={'border': '1px solid black'}
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('offset=1', width={'size': 2, 'offset': 1}, style={'background-color': 'lightblue'}),
                    dbc.Col('offset=2', width={'size': 2, 'offset': 2}, style={'background-color': 'lightskyblue'}),
                    dbc.Col('3', width=2, style={'background-color': '#e88b00'}),
                    dbc.Col('offset=1', width={'size': 2, 'offset': 1}, style={'background-color': '#8c8c8c'})
                ],
                style={'border': '1px solid black'}
            )
        ]
    )
)

if __name__ == '__main__':
    app.run_server()