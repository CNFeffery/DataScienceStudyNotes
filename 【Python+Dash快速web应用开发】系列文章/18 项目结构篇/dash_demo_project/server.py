import dash

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True
)

# 设置网页title
app.title = '七普部分数据看板'

server = app.server