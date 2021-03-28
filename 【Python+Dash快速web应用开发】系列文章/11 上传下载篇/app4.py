import dash
import dash_uploader as du
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

# 配置上传文件夹
du.configure_upload(app, folder='temp')

app.layout = html.Div(
    dbc.Container(
        [
            du.Upload(id='uploader'),
            html.H5('上传中或还未上传文件！', id='upload_status')
        ]
    )
)


@app.callback(
    Output('upload_status', 'children'),
    Input('uploader', 'isCompleted'),
    State('uploader', 'fileNames')
)
def show_upload_status(isCompleted, fileNames):
    if isCompleted:
        return '已完成上传：'+fileNames[0]

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)