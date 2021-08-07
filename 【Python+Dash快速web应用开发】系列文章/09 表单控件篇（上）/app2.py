import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dbc.Input(id='input-number',
                      placeholder='number模式',
                      type='number',
                      min=0,
                      max=100,
                      step=0.5,
                      style={'width': '300px'}),
            html.P(id='output-number'),
            dbc.Input(id='input-range',
                      placeholder='range模式',
                      type='range',
                      style={'width': '300px'},
                      min=0,
                      max=100,
                      step=10,),
            html.P(id='output-range')
        ],
        style={'margin-top': '100px'}
    )
)

@app.callback(
    Output('output-number', 'children'),
    Input('input-number', 'value')
)
def output_number(value):
    return value

@app.callback(
    Output('output-range', 'children'),
    Input('input-range', 'value')
)
def output_range(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)