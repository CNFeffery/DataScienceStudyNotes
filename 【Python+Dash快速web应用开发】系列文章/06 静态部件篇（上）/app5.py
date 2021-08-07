import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        html.Ul(
            [
                html.Br(),
                html.Br(),
                html.Li('1'),
                html.Li('2'),
                html.Ul(
                    [
                        html.Li('2.1'),
                        html.Li('2.2'),
                        html.Li('2.3'),
                        html.Ul(
                            [
                                html.Li('2.1.1'),
                                html.Li('2.1.2'),
                                html.Li('2.1.3'),
                            ]
                        )
                    ]
                ),
                html.Li('3'),
                html.Li('4')
            ]
        )
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)