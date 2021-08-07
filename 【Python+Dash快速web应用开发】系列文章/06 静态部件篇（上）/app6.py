import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        [
            html.H5('（在模仿中精进数据可视化05）疫情期间市值增长top25公司'),
            html.Img(src='https://img2020.cnblogs.com/blog/1344061/202011/1344061-20201129183046286-1089258422.png',
                     style={'width': '100%'})
        ]
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)