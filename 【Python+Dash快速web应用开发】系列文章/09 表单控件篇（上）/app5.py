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
            dbc.Checklist(
                id='check-list-input',
                inline=True,
                options=[
                    {'label': item, 'value': item}
                    for item in list('ABCD')
                ],
                style={
                    'width': '300px'
                }
            ),
            html.P(id='check-list-output')
        ],
        style={'margin-top': '100px'}
    )
)

@app.callback(
    Output('check-list-output', 'children'),
    Input('check-list-input', 'value')
)
def check_list_output(value):

    if value:
        return '已选择：'+'、'.join(value)

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)