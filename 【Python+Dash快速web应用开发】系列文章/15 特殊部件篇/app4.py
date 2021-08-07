import dash
import pandas as pd
import dash_datetimepicker
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dash_datetimepicker.DashDatetimepicker(id="datetime-picker"),
        html.H6(id='datetime-output', style={'margin-top': '20px'})
    ],
    style={
        'margin-top': '100px',
        'max-width': '600px'
    }
)


@app.callback(
    Output('datetime-output', 'children'),
    [Input('datetime-picker', 'startDate'),
     Input('datetime-picker', 'endDate')]
)
def datetime_range(startDate, endDate):
    # 修正8小时时间差bug并格式化为字符串
    startDate = (pd.to_datetime(startDate) + pd.Timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
    endDate = (pd.to_datetime(endDate) + pd.Timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')

    return f'从 {startDate} 到 {endDate}'


if __name__ == "__main__":
    app.run_server(debug=True)
