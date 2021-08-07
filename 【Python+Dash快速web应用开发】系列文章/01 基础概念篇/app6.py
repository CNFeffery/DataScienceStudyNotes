import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

fig = px.scatter(x=range(10), y=range(10), height=400)
fig.update_layout(clickmode='event+select')  # 设置点击模式

app.layout = html.Div(
    [
        dcc.Graph(figure=fig, id='scatter'),
        html.Hr(),
        html.Div([
            '悬浮事件：',
            html.P(id='hover')
        ]),
        html.Hr(),
        html.Div([
            '点击事件：',
            html.P(id='click')
        ]),
        html.Hr(),
        html.Div([
            '选择事件：',
            html.P(id='select')
        ]),
        html.Hr(),
        html.Div([
            '框选事件：',
            html.P(id='zoom')
        ])
    ]
)


# 多对多的回调函数
@app.callback([Output('hover', 'children'),
               Output('click', 'children'),
               Output('select', 'children'),
               Output('zoom', 'children'),],
              [Input('scatter', 'hoverData'),
               Input('scatter', 'clickData'),
               Input('scatter', 'selectedData'),
               Input('scatter', 'relayoutData')])
def listen_to_hover(hoverData, clickData, selectedData, relayoutData):
    return str(hoverData), str(clickData), str(selectedData), str(relayoutData)


if __name__ == '__main__':
    app.run_server()