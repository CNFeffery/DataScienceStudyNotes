import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = dbc.Alert(
    "你好，dash_bootstrap_components！"
)

if __name__ == "__main__":
    app.run_server()