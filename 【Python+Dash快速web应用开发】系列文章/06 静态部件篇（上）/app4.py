import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        html.Ol(
            [
                html.Br(),
                html.Br(),
                html.Li('待办事项1'),
                html.Li('待办事项2'),
                html.Li('待办事项3'),
                html.Li('待办事项4')
            ]
        )
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)