import dash
import dash_uploader as du
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)

# 配置上传文件夹
du.configure_upload(app, folder='temp')

app.layout = html.Div(
    dbc.Container(
        du.Upload()
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)