import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
import re

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.H1('关于Dash用户的调查'),
            html.Br(),

            html.P('1. 您的性别为：'),
            html.Hr(),
            dbc.RadioItems(
                id='gender',
                inline=True,
                options=[
                    {'label': '男', 'value': '男'},
                    {'label': '女', 'value': '女'}
                ]
            ),
            html.Br(),

            html.P('2. 您常用的编程语言有：'),
            html.Hr(),
            dbc.Checklist(
                id='programming-language',
                inline=True,
                options=[
                    {'label': 'Python', 'value': 'Python'},
                    {'label': 'R', 'value': 'R'},
                    {'label': 'JavaScript', 'value': 'JavaScript'},
                    {'label': 'Java', 'value': 'Java'},
                    {'label': 'Julia', 'value': 'Julia'},
                    {'label': 'C#', 'value': 'C#'},
                    {'label': 'C++', 'value': 'C++'},
                    {'label': '其他', 'value': '其他'},
                ]
            ),
            html.Br(),

            html.P('3. 您使用Dash的频繁程度：'),
            html.Hr(),
            dbc.RadioItems(
                id='frequency',
                inline=True,
                options=[
                    {'label': '经常', 'value': '经常'},
                    {'label': '偶尔', 'value': '偶尔'},
                    {'label': '很少使用', 'value': '很少使用'},
                    {'label': '没听说过', 'value': '没听说过'},
                ]
            ),
            html.Br(),

            html.P('4. 您对以下哪些方面感兴趣：'),
            html.Hr(),
            dbc.Checklist(
                id='interests',
                options=[
                    {'label': '构建在线数据可视化作品', 'value': '构建在线数据可视化作品'},
                    {'label': '制作机器学习demo', 'value': '制作机器学习demo'},
                    {'label': '为企业开发BI仪表盘', 'value': '为企业开发BI仪表盘'},
                    {'label': '为企业开发酷炫的指标监控大屏', 'value': '为企业开发酷炫的指标监控大屏'},
                    {'label': '开发有用的在线小工具', 'value': '开发有用的在线小工具'},
                    {'label': '其他', 'value': '其他'},
                ]
            ),
            html.Br(),

            html.P('5. 您的职业：'),
            html.Hr(),
            dbc.RadioItems(
                id='career',
                options=[
                    {'label': '科研人员', 'value': '科研人员'},
                    {'label': '运营', 'value': '运营'},
                    {'label': '数据分析师', 'value': '数据分析师'},
                    {'label': '算法工程师', 'value': '算法工程师'},
                    {'label': '大数据开发工程师', 'value': '大数据开发工程师'},
                    {'label': '金融分析师', 'value': '金融分析师'},
                    {'label': '爬虫工程师', 'value': '爬虫工程师'},
                    {'label': '学生', 'value': '学生'},
                    {'label': '其他', 'value': '其他'},
                ]
            ),
            html.Br(),

            html.P('您的联系方式：'),
            html.Hr(),
            dbc.Input(
                id='tel',
                placeholder='填入您的电话或手机号码！',
                autoComplete='off', # 关闭浏览器自动补全
                style={
                    'width': '300px'
                }
            ),
            html.Hr(),

            dbc.Button(
                '点击提交',
                id='submit'
            ),

            html.P(id='feedback')

        ],
        style={
            'margin-top': '50px',
            'margin-bottom': '200px',
        }
    )
)


@app.callback(
    Output('feedback', 'children'),
    Input('submit', 'n_clicks'),
    [
        State('gender', 'value'),
        State('programming-language', 'value'),
        State('frequency', 'value'),
        State('interests', 'value'),
        State('tel', 'value'),
    ],
    prevent_initial_call=True
)
def fetch_info(n_clicks, gender, programming_language, frequency, interests, tel):
    if all([gender, programming_language, frequency, interests, tel]):

        # 简单以写出到本地指定json文件为例来演示写出过程
        with open(tel+'.json', 'w') as j:
            json.dump(
                {
                    'gender': gender,
                    'programming_language': programming_language,
                    'frequency': frequency,
                    'interests': interests
                },
                j
            )
        return '提交成功！'

    else:
        return '您的信息未填写完整，请检查后提交！'

@app.callback(
    [Output('tel', 'valid'),
     Output('tel', 'invalid')],
    Input('tel', 'value'),
    prevent_initial_call=True
)
def check_if_tel_completed(value):
    try:
        if re.findall('\d+', value)[0] == value and value.__len__() == 11:
            return True, False
    except:
        pass

    return False, True

if __name__ == '__main__':
    app.run_server(debug=True)