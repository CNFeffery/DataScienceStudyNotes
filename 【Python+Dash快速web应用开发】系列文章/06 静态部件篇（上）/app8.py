import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Iframe(src='https://www.baidu.com/',
                        style={'width': '100%', 'height': '800px'})
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)