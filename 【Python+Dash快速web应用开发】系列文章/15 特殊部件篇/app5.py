import dash
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

app = dash.Dash(__name__)

builderJson = {
    "all": 10887,
    "charts": {
        "map": 3237,
        "lines": 2164,
        "bar": 7561,
        "line": 7778,
        "pie": 7355,
        "scatter": 2405,
        "candlestick": 1842,
        "radar": 2090,
        "heatmap": 1762,
        "treemap": 1593,
        "graph": 2060,
        "boxplot": 1537,
        "parallel": 1908,
        "gauge": 2107,
        "funnel": 1692,
        "sankey": 1568
    },
    "components": {
        "geo": 2788,
        "title": 9575,
        "legend": 9400,
        "tooltip": 9466,
        "grid": 9266,
        "markPoint": 3419,
        "markLine": 2984,
        "timeline": 2739,
        "dataZoom": 2744,
        "visualMap": 2466,
        "toolbox": 3034,
        "polar": 1945
    },
    "ie": 9743
}

downloadJson = {
    "echarts.min.js": 17365,
    "echarts.simple.min.js": 4079,
    "echarts.common.min.js": 6929,
    "echarts.js": 14890
}

themeJson = {
    "dark.js": 1594,
    "infographic.js": 925,
    "shine.js": 1608,
    "roma.js": 721,
    "macarons.js": 2179,
    "vintage.js": 1982
}

app.layout = dbc.Container(
    [
        html.Div(
            [
                html.H1(id='n-weeks'),
                html.Div(id='demo', style={'width': '100%', 'height': '80%'})
            ],
            style={'height': '100vh', 'width': '100%'}
        ),
        dcc.Interval(id='interval', n_intervals=1),
        dcc.Store(id='live-data',
                  data={
                      'builderJson': builderJson,
                      'downloadJson': downloadJson,
                      'themeJson': themeJson
                  })
    ]
)


@app.callback(
    Output('n-weeks', 'children'),
    Input('interval', 'n_intervals')
)
def update_header(n_intervals):
    if n_intervals:
        return f'2021年第{n_intervals}周使用量统计：'

    return dash.no_update


@app.callback(
    Output('live-data', 'data'),
    Input('interval', 'n_intervals'),
    State('live-data', 'data')
)
def update_live_data(n_intervals, data):
    # 随机更新数据
    for key1 in data['builderJson'].keys():
        if isinstance(data['builderJson'][key1], dict):
            for key2 in data['builderJson'][key1].keys():
                data['builderJson'][key1][key2] += np.random.randint(-50, 50)

        else:
            data['builderJson'][key1] += np.random.randint(-50, 50)

    for key in data['downloadJson'].keys():
        data['downloadJson'][key] += np.random.randint(-50, 50)

    for key in data['themeJson'].keys():
        data['themeJson'][key] += np.random.randint(-50, 50)

    return data


app.clientside_callback(
    # 关联自编js脚本中的相应回调函数
    ClientsideFunction(
        namespace='clientside',
        function_name='live_update'
    ),
    Output('demo', 'children'),
    Input('live-data', 'data'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
