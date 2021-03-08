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
                ]
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col('order=last', width={'size': 2, 'order': 'last'}, style={'background-color': 'lightblue'}),
                    dbc.Col('order=2', width={'size': 2, 'order': 2}, style={'background-color': 'lightskyblue'}),
                    dbc.Col('order=1', width={'size': 2, 'order': 1}, style={'background-color': '#e88b00'}),
                    dbc.Col('order=first', width={'size': 2, 'order': 'first'}, style={'background-color': '#8c8c8c'})
                ]
            )
        ]
    )
)

if __name__ == '__main__':
    app.run_server()