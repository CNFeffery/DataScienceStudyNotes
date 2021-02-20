import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.H1('静态部件示例'),
            html.Hr(),
            html.H2('这是二级标题'),
            html.H3('这是三级标题'),
            html.H4('这是四级标题'),
            html.P(
                [
                    '这是一个',
                    html.A('链接', href='#'),
                    '，而这是一段',
                    html.Strong('加粗文字'),
                    '，这是一段带上下标的文字：',
                    '测试',
                    html.Sup('上标'),
                    '，测试',
                    html.Sub('下标')
                ]
            ),

            html.Img(src='https://img2020.cnblogs.com/blog/1344061/202102/1344061-20210207194037614-808613819.png'),

            html.Br(),
            html.H1('交互部件示例'),
            html.Br(),
            dcc.Dropdown(
                options=[
                    {'label': '测试1', 'value': '测试1'},
                    {'label': '测试2', 'value': '测试2'},
                    {'label': '测试3', 'value': '测试3'},
                ]),
            html.Br(),
            dcc.Checklist(
                options=[
                    {'label': '测试1', 'value': '测试1'},
                    {'label': '测试2', 'value': '测试2'},
                    {'label': '测试3', 'value': '测试3'},
                ],
                value=['测试1']
            ),
            html.Br(),
            dcc.RangeSlider(
                min=0,
                max=20,
                step=0.01,
                value=[5, 15]
            )
        ]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)