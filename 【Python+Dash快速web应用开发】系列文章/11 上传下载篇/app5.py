from flask import send_from_directory
import dash
import dash_uploader as du
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import os

app = dash.Dash(__name__)

du.configure_upload(app, 'temp', use_upload_id=False)

app.layout = html.Div(
    dbc.Container(
        [
            du.Upload(id='upload'),
            html.Div(
                id='download-files'
            )
        ]
    )
)

@app.server.route('/download/<file>')
def download(file):

    return send_from_directory('temp', file)

@app.callback(
    Output('download-files', 'children'),
    Input('upload', 'isCompleted')
)
def render_download_url(isCompleted):

    if isCompleted:
        return html.Ul(
            [
                html.Li(html.A(f'/{file}', href=f'/download/{file}', target='_blank'))
                for file in os.listdir('temp')
            ]
        )

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)