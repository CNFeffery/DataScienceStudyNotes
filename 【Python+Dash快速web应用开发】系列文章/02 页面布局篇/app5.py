import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col('第一行'),
                style={
                    'background-color': 'lightgreen'
                }),
        dbc.Row(
            [
                dbc.Col('第二行第一列', width=6, style={'background-color': 'lightblue'}),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Col('嵌套1', width=6, style={'background-color': 'Moccasin'}),
                            dbc.Col('嵌套2', width=3, style={'background-color': 'lightskyblue'}),
                            dbc.Col('嵌套3', width=3, style={'background-color': 'Moccasin'}),
                        ]
                    ),
                    width=6,
                    style={'background-color': 'lightskyblue'})
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server()