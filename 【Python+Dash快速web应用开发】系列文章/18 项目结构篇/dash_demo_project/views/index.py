import dash_html_components as html

from server import app

index_page = html.Div(
    [
        html.P(
            [
                html.Span('欢迎来到基于'),
                html.Strong('plotly dash', style={'color': 'rgb(13, 103, 180)'}),
                html.Em(html.Sup('[1]', style={'fontSize': '16px'})),
                html.Span('编写的'),
                html.Strong('全国第七次人口普查'),
                html.Span('部分数据'),
                html.Em(html.Sup('[2]', style={'fontSize': '16px'})),
                html.Span('简易看板示例，'),
                html.Span('作者'),
                html.A('费弗里', href='https://github.com/CNFeffery', target='_blank'),
                html.Span('。')
            ],
            id='index-desc',
            style={
                'margin': '50px 0 50px 50px'
            }
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Span('知识星球【我们谈论数据科学】：', style={'fontWeight': 'bold', 'fontSize': '10px'}),
                        html.Img(src=app.get_asset_url('img/zsxq.png'), style={'width': '100%'})
                    ],
                    style={
                        'flex': 'none',
                        'width': '250px',
                        'marginRight': '75px'
                    }
                ),
                html.Div(
                    [
                        html.Span('微信公众号【Python大数据分析】：', style={'fontWeight': 'bold', 'fontSize': '10px'}),
                        html.Img(src=app.get_asset_url('img/wxgzh.png'), style={'width': '100%'})
                    ],
                    style={
                        'flex': 'none',
                        'width': '250px',
                        'marginLeft': '75px'
                    }
                )
            ],
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'borderTop': '1px solid #e0e0e0',
                'borderBottom': '1px solid #e0e0e0',
                'margin': '0 50px 0 50px'
            }
        ),
        html.P(
            [
                html.Em('[1] '),
                html.Span('一个面向数据分析相关人员，纯Python即可实现交互式web应用，极大程度上简化web应用开发难度的先进框架，欢迎前往最详细的中文教程'),
                html.A('https://www.cnblogs.com/feffery/tag/Dash/',
                       href='https://www.cnblogs.com/feffery/tag/Dash/',
                       target='_blank'),
                html.Br(),
                html.Span('或关注微信公众号：'),
                html.Strong('Python大数据分析'),
                html.Span('学习相关知识'),
                html.Br(),
                html.Br(),
                html.Em('[2] '),
                html.Span('数据来源：'),
                html.A('https://www.heywhale.com/mw/dataset/609b77f306b94200178fbd4d/file',
                       href='https://www.heywhale.com/mw/dataset/609b77f306b94200178fbd4d/file',
                       target='_blank')
            ],
            style={
                'margin': '50px 0 0 50px'
            }
        )
    ]
)
