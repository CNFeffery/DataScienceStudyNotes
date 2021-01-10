import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('根据省名查询省会城市：'),
        html.Br(),
        dcc.Dropdown(
            id='province',
            options=[
                {'label': '四川省', 'value': '四川省'},
                {'label': '陕西省', 'value': '陕西省'},
                {'label': '广东省', 'value': '广东省'}
            ],
            value='四川省'
        ),
        html.P(id='city')
    ]
)

province2city_dict = {
    '四川省': '成都市',
    '陕西省': '西安市',
    '广东省': '广州市'
}

@app.callback(Output('city', 'children'),
              Input('province', 'value'))
def province2city(province):

    return province2city_dict[province]

if __name__ == '__main__':
    app.run_server()