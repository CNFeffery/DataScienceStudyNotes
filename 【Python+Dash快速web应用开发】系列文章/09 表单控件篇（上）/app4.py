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
            dbc.RadioItems(
                id='radio-items-input',
                inline=True,
                switch=True,
                options=[
                    {'label': item, 'value': item}
                    for item in list('ABCD')
                ],
                style={
                    'width': '300px'
                }
            ),
            html.P(id='radio-items-output')
        ],
        style={'margin-top': '100px'}
    )
)

@app.callback(
    Output('radio-items-output', 'children'),
    Input('radio-items-input', 'value')
)
def radio_items_output(value):

    if value:
        return '已选择：'+value

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)