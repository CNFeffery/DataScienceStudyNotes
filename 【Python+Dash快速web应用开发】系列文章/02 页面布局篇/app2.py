import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    # 直接填写assets下css文件路径+文件名
    external_stylesheets=['css/bootstrap.min.css']
)

app.layout = dbc.Alert(
    "你好，dash_bootstrap_components！"
)

if __name__ == "__main__":
    app.run_server()