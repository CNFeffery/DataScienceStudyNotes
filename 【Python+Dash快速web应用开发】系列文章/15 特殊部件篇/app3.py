import dash
import dash_daq as daq
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        daq.ColorPicker(
            id='color-picker',
            label={
                'label': '色彩选择器',
                'style': {
                    'font-size': '18px',
                    'font-family': 'SimHei',
                    'font-weight': 'bold'
                }
            },
            size=400,
            value=dict(hex="#120E03")
        ),
        html.P(
            '测试'*100,
            id='demo-p',
            style={
                'margin-top': '20px'
            }
        )
    ],
    style={
        'margin-top': '30px',
        'max-width': '500px'
    }
)

app.clientside_callback(
    """
    function(color) {
        return {'color': color.hex, 'margin-top': '20px'};
    }
    """,
    Output('demo-p', 'style'),
    Input('color-picker', 'value')
)

if __name__ == '__main__':
    app.run_server(debug=True)
