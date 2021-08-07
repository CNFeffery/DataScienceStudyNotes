import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    dcc.Textarea(
                        id='md-input',
                        placeholder='请输入你的markdown源码！',
                        style={
                            'width': '100%',
                            'height': '100%'
                        }
                    ),
                    width=6,
                    style={
                        'padding-right': 0,
                        'border': 'border:5px solid red'
                    }
                ),
                dbc.Col(
                    dcc.Markdown(id='md-output',
                                 dangerously_allow_html=True,
                                 style={
                                     'position': 'absolute',
                                     'width': '100%',
                                     'height': '100%'
                                 }),
                    width=6,
                    style={
                        'position': 'relative',
                        'overflow': 'auto',
                        'padding-left': 0
                    }
                ),
            ],
            style={
                'position': 'fixed',
                'top': 0,
                'bottom': 0,
                'left': 0,
                'right': 0
            }
        )
    ),
    style={
        'font-size': '2rem'
    }
)


@app.callback(
    Output('md-output', 'children'),
    Input('md-input', 'value')
)
def online_markdown(raw_text):
    return raw_text


if __name__ == '__main__':
    app.run_server(debug=True)