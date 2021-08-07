import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        html.Blockquote(
            html.P('这是一段由块引用包裹的文字内容' * 10),
            style={
                'background-color': 'rgba(211, 211, 211, 0.25)',
                'text-indent': '3rem'
            }
        )
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)