import dash
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        html.P(
            [
                html.Strong('贵州茅台(600519)'),
                '最新股价：',
                html.Span('2108.94', id='latest-price')
            ]
        ),
        dcc.Interval(id='demo-interval', interval=1000)
    ],
    style={
        'margin-top': '100px'
    }
)


@app.callback(
    [Output('latest-price', 'children'),
     Output('latest-price', 'style')],
    Input('demo-interval', 'n_intervals'),
    State('latest-price', 'children')
)
def fake_price_generator(n_intervals, latest_price):
    fake_price = float(latest_price) + np.random.normal(0, 0.1)

    if fake_price > float(latest_price):
        return f'{fake_price:.2f}', {'color': 'red', 'background-color': 'rgba(195, 8, 26, 0.2)'}

    elif fake_price < float(latest_price):
        return f'{fake_price:.2f}', {'color': 'green', 'background-color': 'rgba(50, 115, 80, 0.2)'}

    return f'{fake_price:.2f}', {'background-color': 'rgba(113, 120, 117, 0.2)'}


if __name__ == '__main__':
    app.run_server(debug=True)
