import dash
import dash_uploader as du
import dash_bootstrap_components as dbc
import dash_html_components as html

import uuid

app = dash.Dash(__name__)

# 配置上传文件夹
du.configure_upload(app, folder='temp')

def render_random_id_uploader():

    return du.Upload(
            id='uploader',
            text='点击或拖动文件到此进行上传！',
            text_completed='已完成上传文件：',
            cancel_button=True,
            pause_button=True,
            filetypes=['md', 'mp4'],
            default_style={
                'background-color': '#fafafa',
                'font-weight': 'bold'
            },
            upload_id=uuid.uuid1()
        )

def render_layout():

    return html.Div(
    dbc.Container(
        render_random_id_uploader()
    )
)

app.layout = render_layout

if __name__ == '__main__':
    app.run_server(debug=True)