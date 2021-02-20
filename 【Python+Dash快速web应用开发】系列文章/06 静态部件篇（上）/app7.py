import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.H5('音频示例：'),
            html.Audio(src='https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3',
                       controls=True),
            html.H5('视频示例：'),
            html.Video(src='https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4',
                       controls=True,
                       style={'width': '100%'}),
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)