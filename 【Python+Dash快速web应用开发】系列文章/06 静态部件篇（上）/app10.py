import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            dcc.Markdown('''
> 本文示例代码已上传至我的`Github`仓库[https://github.com/CNFeffery/DataScienceStudyNotes](https://github.com/CNFeffery/DataScienceStudyNotes)

# 1 简介

　　 这是我的系列教程**Python+Dash快速web应用开发**的第五期，在上一期的文章中，我们针对`Dash`中有关回调的一些技巧性的特性进行了介绍，使得我们可以更愉快地为`Dash`应用编写回调交互功能。

　　而今天的文章作为**回调交互**系统性内容的最后一期，我将带大家get一些`Dash`中实际应用效果惊人的**高级回调特性**，系好安全带，我们起飞~

<p align="center"><img src="https://img2020.cnblogs.com/blog/1344061/202102/1344061-20210207194037614-808613819.png" style="zoom:100%;" /></p>

''',
                         dangerously_allow_html=True,
                         dedent=False)
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)