import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_core_components as dcc
import json

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dcc.Dropdown(
                id='dropdown-input-1',
                placeholder='单选',
                options=[
                    {'label': item, 'value': item}
                    for item in list('ABCD')
                ],
                style={
                    'width': '300px'
                }
            ),
            html.Pre(id='dropdown-output-1',
                     style={'background-color': '#d4d4d420',
                            'width': '300px'}),
            dcc.Dropdown(
                id='dropdown-input-2',
                placeholder='多选',
                multi=True,
                options=[
                    {'label': item, 'value': item}
                    for item in list('ABCD')
                ],
                style={
                    'width': '300px'
                }
            ),
            html.Pre(id='dropdown-output-2',
                     style={'background-color': '#d4d4d420',
                            'width': '300px'})
        ],
        style={'margin-top': '100px'}
    )
)

@app.callback(
    Output('dropdown-output-1', 'children'),
    Input('dropdown-input-1', 'value')
)
def dropdown_output_1(value):
    if value:
        return json.dumps(value, indent=4)

    return dash.no_update

@app.callback(
    Output('dropdown-output-2', 'children'),
    Input('dropdown-input-2', 'value')
)
def dropdown_output_2(value):
    if value:
        return json.dumps(value, indent=4)

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)