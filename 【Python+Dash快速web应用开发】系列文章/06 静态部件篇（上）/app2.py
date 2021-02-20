import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.H1('一级标题', id='demo1'),
            html.H2('二级标题'),
            html.H3('三级标题'),
            html.H4('四级标题'),
            html.H5('五级标题'),
            html.H6('六级标题'),
            html.Br(), # 换行
            html.Hr(), # 水平分割线
            html.P('这是一段文字。'*20),
            html.P('这是另一段带有首行缩进的文字。'*10, style={'text-indent': '3rem'}),
            html.A('跳转到费弗里的Github仓库',
                   target='_blank',
                   href='https://github.com/CNFeffery/DataScienceStudyNotes'), # 跳转到外部链接
            html.Br(),
            html.A('跳转到六级标题', href='#demo2'),
            html.P(
                [
                    '一段文字中出现了',
                    html.I('斜体'),
                    '，以及代码片段',
                    html.Code('import dash'),
                    '，还有一段',
                    html.U('带下划线的文字'),
                    '，一段',
                    html.Mark('高亮标注文字'),
                    '，以及另一段',
                    html.Mark('不同颜色的高亮标注文字。', style={'background-color': 'lightblue'})
                 ]
            )
        ] + [html.Br()] * 50 + [html.A('回到顶端一级标题', href='#demo1'),
                                html.H1('页内元素跳转示例标题', id='demo2')]
    )
)


if __name__ == '__main__':
    app.run_server(debug=True)