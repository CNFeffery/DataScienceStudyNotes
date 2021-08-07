import dash
import dash_html_components as html
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import time

app = dash.Dash(
    __name__,
    # external_stylesheets=['css/bootstrap.min.css'],
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    dbc.Container(
        [
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("贷款金额", addon_type="prepend"),
                            dbc.Input(
                                id='loan_amount',
                                placeholder='请输入贷款总金额',
                                type="number",
                                value=100
                            ),
                            dbc.InputGroupAddon("万元", addon_type="append"),
                        ],
                    ),
                    width={'size': 6, 'offset': 3}
                )
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("计划还款月数", addon_type="prepend"),
                            dbc.Input(
                                id='repay_month_amount',
                                placeholder='请输入计划还款月数',
                                type="number",
                                value=24,
                                min=1,
                                step=1
                            ),
                            dbc.InputGroupAddon("个月", addon_type="append"),
                        ],
                    ),
                    width={'size': 6, 'offset': 3}
                )
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("年利率", addon_type="prepend"),
                            dbc.Input(
                                id='interest_rate',
                                placeholder='请输入年利率',
                                type="number",
                                value=5,
                                min=0,
                                step=0.001
                            ),
                            dbc.InputGroupAddon("%", addon_type="append"),
                        ],
                    ),
                    width={'size': 6, 'offset': 3}
                )
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.RadioItems(
                        id="repay_method",
                        options=[
                            {"label": "等额本息", "value": "等额本息"},
                            {"label": "等额本金", "value": "等额本金"}
                        ],
                        value='等额本息'
                    ),
                    width={'size': 6, 'offset': 3}
                ),
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.Button('开始计算', id='start', n_clicks=0, color='light'),
                    width={'size': 6, 'offset': 3}
                ),
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dcc.Loading(dcc.Graph(id='repay_timeline')),
                    width={'size': 6, 'offset': 3}
                ),
            ),
        ],
        fluid=True
    )
)


def make_line_graph(loan_amount,
                    repay_month_amount,
                    interest_rate,
                    repay_method):
    interest_rate /= 100
    loan_amount *= 10000

    month_interest_rate = interest_rate / 12

    if repay_method == '等额本息':

        month_repay = loan_amount * month_interest_rate * pow((1 + month_interest_rate), repay_month_amount) / \
                      (pow((1 + month_interest_rate), repay_month_amount) - 1)

        month_repay = round(month_repay, 2)

        month_repay = [month_repay] * repay_month_amount

    else:

        d = loan_amount / repay_month_amount
        month_repay = [round(d + (loan_amount - d * (month - 1)) * month_interest_rate, 3)
                       for month in range(1, repay_month_amount + 1)]

    fig = px.line(x=[f'第{i}月' for i in range(1, repay_month_amount + 1)],
                  y=month_repay,
                  title='每月还款金额变化曲线（总支出：{}元）'.format(round(sum(month_repay), 2)),
                  template='plotly_white')

    return fig

@app.callback(
    Output('repay_timeline', 'figure'),
    Input('start', 'n_clicks'),
    [State('loan_amount', 'value'),
     State('repay_month_amount', 'value'),
     State('interest_rate', 'value'),
     State('repay_method', 'value')],
    prevent_initial_call=True
)
def refresh_repay_timeline(n_clicks, loan_amount, repay_month_amount, interest_rate, repay_method):
    time.sleep(0.2) # 增加应用的动态效果

    return make_line_graph(loan_amount, repay_month_amount, interest_rate, repay_method)


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)