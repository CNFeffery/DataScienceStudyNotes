import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import requests

# 爬取LIL官网后台英雄列表信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

target = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

hero_list = requests.get(target, headers=headers).json()

def query_hero_info(hero_id):
    '''
    根据英雄id获取指定英雄的资料数据
    '''

    hero_info = requests.get('https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js' % hero_id,
                             headers=headers).json()

    return hero_info

# 这里用external_scripts导入最后的轮播图所需的js依赖
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=False,
    external_scripts=["https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js",
                      "https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js",
                      "https://cdn.staticfile.org/twitter-bootstrap/4.3.1/js/bootstrap.min.js"]
)

# 构建应用
app.layout = html.Div(
    dbc.Container(
        [
            dbc.Form(
                [
                    # 英雄选择控件
                    dbc.FormGroup(
                        [
                            dbc.Label('选择英雄名称：', html_for='hero_list'),
                            dcc.Dropdown(id='hero_list',
                                         options=[
                                             {'label': item['name'], 'value': item['heroId']}
                                             for item in hero_list['hero']
                                         ])
                        ]
                    ),

                    # 查看内容选择空间
                    dbc.FormGroup(
                        [
                            dbc.Label('选择要查看的内容：', html_for='hero_attributes'),
                            dcc.Dropdown(id='hero_attributes',
                                         multi=True,
                                         options=[
                                             {'label': item, 'value': item}
                                             for item in ['基础属性', '技能介绍', '皮肤一览']
                                         ])
                        ]
                    ),

                    # 提交查询按钮
                    dbc.FormGroup(
                        [
                            dbc.Button('查　询', id='query')
                        ]
                    )
                ]
            ),

            # 将渲染的内容包裹在Spinner中实现加载动画
            dbc.Spinner(
                dbc.Tabs(
                    id='hero_attributes_list'
                )
            )
        ],
        style={
            'margin-top': '30px',
            'max-width': '800px'
        }
    )
)

@app.callback(
    Output('hero_attributes_list', 'children'),
    Input('query', 'n_clicks'),
    [State('hero_list', 'value'),
     State('hero_attributes', 'value')]
)
def render_content(n_clicks, hero_id, hero_attributes):
    '''
    根据用户控件输入结果，进行相应查询结果的渲染
    :param n_clicks: 查询按钮点击次数
    :param hero_id: 已选择的英雄对应id
    :param hero_attributes: 已选择要展示的内容范围
    :return:
    '''

    # 当按钮被新一轮点击后
    if n_clicks:
        # 当hero_id与hero_attributes不为空时
        if hero_id and hero_attributes:

            # 获取该英雄全部信息
            hero_info = query_hero_info(hero_id)

            # 初始化Tabs返回结果
            tabs = []
            if '基础属性' in hero_attributes:
                # 渲染基础属性面板内容
                tabs.append(
                    dbc.Tab(
                        [
                            html.H2(hero_info['hero']['name']),
                            html.H5(hero_info['hero']['title']),
                            html.H6(hero_info['hero']['alias']),
                            html.P(
                                ' '.join([
                                    '基础生命值：' + hero_info['hero']['hp'].split('.')[0],
                                    '基础法力值：' + hero_info['hero']['mp'].split('.')[0],
                                    '基础移速：' + hero_info['hero']['movespeed'].split('.')[0],
                                    '基础攻击力：' + hero_info['hero']['attackdamage'].split('.')[0]
                                ])
                            ),
                            html.Img(
                                src=hero_info['skins'][0]['mainImg'],
                                style={'width': '100%'}
                            )
                        ],
                        label='基础属性'
                    )
                )

            if '技能介绍' in hero_attributes:
                # 渲染技能介绍面板内容

                # 自定义排序，以方便取出对应正常技能顺序的技能介绍
                CUSTOM_ORDER = {"passive": 0, "q": 1, "w": 2, 'e': 3, 'r': 4}
                skills = sorted(hero_info['spells'], key=lambda item: CUSTOM_ORDER[item['spellKey']])

                tabs.append(
                    dbc.Tab(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(html.Img(src=skill['abilityIconPath']), width=1),
                                    dbc.Col([html.P(skill['spellKey'].upper().replace('PASSIVE', '被动') +
                                                    '技能：' + skill['name'], style={'font-weight': 'bold'}),
                                             html.P(skill['description'])])
                                ],
                                justify='start'
                            )
                            for skill in skills
                        ],
                        label='技能介绍'
                    )
                )

            if '皮肤一览' in hero_attributes:

                # 渲染皮肤一览面板内容

                hero_info['skins'] = [skin for skin in hero_info['skins'] if skin['mainImg'] != '']

                # 该部分参考https://www.runoob.com/try/try.php?filename=trybs4_carousel#demo，并移植为Dash代码
                tabs.append(
                    dbc.Tab(
                        [
                            html.Div(
                                [
                                    html.Ul(
                                        [
                                            html.Li(**{
                                                'data-target': '#demo',
                                                'data-slide-to': '0',
                                                'className': 'active'
                                            })
                                        ] +
                                        [
                                            html.Li(**{
                                                'data-target': '#demo',
                                                'data-slide-to': str(i)
                                            })
                                            for i in range(1, hero_info['skins'].__len__() + 1)
                                        ],
                                        className='carousel-indicators'
                                    ),

                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Img(
                                                        src=hero_info['skins'][0]['mainImg']
                                                    ),
                                                    html.Div(
                                                        html.H2(hero_info['skins'][0]['name']),
                                                        className='carousel-caption'
                                                    )
                                                ],
                                                className='carousel-item active'
                                            )
                                        ] + [
                                            html.Div(
                                                [
                                                    html.Img(
                                                        src=skin['mainImg']
                                                    ),
                                                    html.Div(
                                                        html.H2(skin['name']),
                                                        className='carousel-caption'
                                                    )
                                                ],
                                                className='carousel-item'
                                            )
                                            for skin in hero_info['skins'][1:]
                                        ],
                                        className='carousel-inner'
                                    ),

                                    html.A(
                                        html.Span(className='carousel-control-prev-icon'),
                                        className='carousel-control-prev',
                                        href='#demo',
                                        **{'data-slide': 'prev'}
                                    ),

                                    html.A(
                                        html.Span(className='carousel-control-next-icon'),
                                        className='carousel-control-next',
                                        href='#demo',
                                        **{'data-slide': 'next'}
                                    )
                                ],
                                id='demo',
                                className='carousel slide',
                                **{'data-ride': 'carousel'}
                            )
                        ],
                        label='皮肤一览'
                    )
                )

            # 返回渲染结果
            return tabs

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)