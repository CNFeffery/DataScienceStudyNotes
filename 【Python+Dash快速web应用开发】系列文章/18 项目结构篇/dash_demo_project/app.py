import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from server import app

from views.index import index_page
from views.age import age_page
from views.sex import sex_page
from views.statistics import statistics_page

app.layout = html.Div(
    [
        # 监听url变化
        dcc.Location(id='url'),
        html.Div(
            [
                # 标题区域
                html.Div(
                    html.H3(
                        '七普部分数据看板',
                        style={
                            'marginTop': '20px',
                            'fontFamily': 'SimSun',
                            'fontWeight': 'bold'
                        }
                    ),
                    style={
                        'textAlign': 'center',
                        'margin': '0 10px 0 10px',
                        'borderBottom': '2px solid black'
                    }
                ),

                # 子页面区域
                html.Hr(),

                dbc.Nav(
                    [
                        dbc.NavLink('首页', href='/', active="exact"),
                        dbc.NavLink('年龄结构', href='/age', active="exact"),
                        dbc.NavLink('性别结构', href='/sex', active="exact"),
                        dbc.NavLink('六普vs七普', href='/statistics', active="exact"),
                    ],
                    vertical=True,
                    pills=True
                )
            ],
            style={
                'flex': 'none',
                'width': '300px',
                'backgroundColor': '#fafafa'
            }
        ),
        html.Div(
            id='page-content',
            style={
                'flex': 'auto'
            }
        )
    ],
    style={
        'width': '100vw',
        'height': '100vh',
        'display': 'flex'
    }
)


# 路由总控
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_page_content(pathname):
    if pathname == '/':
        return index_page

    elif pathname == '/age':
        return age_page

    elif pathname == '/sex':
        return sex_page

    elif pathname == '/statistics':
        return statistics_page

    return html.H1('您访问的页面不存在！')


if __name__ == '__main__':
    app.run_server(debug=False)
