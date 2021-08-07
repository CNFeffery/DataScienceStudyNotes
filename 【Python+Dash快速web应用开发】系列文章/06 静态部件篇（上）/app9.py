import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            dcc.Textarea(style={'width': '100%', 'height': '300px'},
                         id='input',
                         value='',
                         placeholder='请输入文字内容！'),
            html.P(id='output')
        ]
    )
)

@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def mask_dirty_talk(value):

    return value.replace('他妈', '**')


if __name__ == "__main__":
    app.run_server(debug=True)