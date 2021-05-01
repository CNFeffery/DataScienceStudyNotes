import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html  # 用于直接渲染html源码字符串
from dash.dependencies import Input, Output

import re
from html import unescape
import requests
from lxml import etree

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    dbc.Spinner(
        dbc.Container(
            [
                dcc.Location(id='url'),

                html.Div(
                    id='page-content'
                )
            ],
            style={
                'paddingTop': '30px',
                'paddingBottom': '50px',
                'borderRadius': '10px',
                'boxShadow': 'rgb(0 0 0 / 20%) 0px 13px 30px, rgb(255 255 255 / 80%) 0px -13px 30px'
            }
        ),
        fullscreen=True
    )
)


@app.callback(
    Output('article-links', 'children'),
    Input('url', 'pathname')
)
def render_article_links(pathname):
    response = requests.get('https://www.cnblogs.com/feffery/tag/Dash/',
                            headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
                            })

    tree = etree.HTML(response.text)

    posts = [
        (href, title.strip())
        for href, title in zip(
            tree.xpath("//div[@class='postTitl2']/a/@href"),
            tree.xpath("//div[@class='postTitl2']/a/span/text()")
        )
    ]

    return [
        html.Li(
            dcc.Link(title, href=f'/article-{href.split("/")[-1]}', target='_blank')
        )
        for href, title in posts
    ]


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def render_article_content(pathname):
    if pathname == '/':

        return [
            html.H2('博客列表：'),

            html.Div(
                id='article-links',
                style={
                    'width': '100%'
                }
            )
        ]

    elif pathname.startswith('/article-'):

        response = requests.get('https://www.cnblogs.com/feffery/p/%s.html' % re.findall('\d+', pathname)[0])

        tree = etree.HTML(response.text)

        return (
            html.H3(tree.xpath("//title/text()")[0].split(' - ')[0]),
            html.Em('作者：费弗里'),
            dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
                unescape(etree.tostring(tree.xpath('//div[@id="cnblogs_post_body"]')[0]).decode())
            )
        )

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
