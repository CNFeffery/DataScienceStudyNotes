import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ALL
import re
import json

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.InputGroup(
                            [
                                dbc.InputGroupAddon("金额", addon_type="prepend"),
                                dbc.Input(
                                    id='account-amount',
                                    placeholder='请输入金额',
                                    type="number",
                                ),
                                dbc.InputGroupAddon("元", addon_type="append"),
                            ],
                        ),
                        width=5
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='account-type',
                            options=[
                                {'label': '生活开销', 'value': '生活开销'},
                                {'label': '人情往来', 'value': '人情往来'},
                                {'label': '医疗保健', 'value': '医疗保健'},
                                {'label': '旅游休闲', 'value': '旅游休闲'},
                            ],
                            placeholder='请选择类型：'
                        ),
                        width=5
                    ),
                    dbc.Col(
                        dbc.Button('提交记录', id='account-submit'),
                        width=2
                    )
                ]
            )
        ),
        html.Br(),
        dbc.Container([], id='account-record-container'),
        dbc.Container('暂无记录！', id='account-record-sum'),
        dbc.Container(html.Pre('{}', id='raw-json'))
    ]
)


@app.callback(
    Output('account-record-container', 'children'),
    Input('account-submit', 'n_clicks'),
    [State('account-record-container', 'children'),
     State('account-amount', 'value'),
     State('account-type', 'value')],
    prevent_initial_call=True
)
def update_account_records(n_clicks, children, account_amount, account_type):
    '''
    用于处理每一次的记账输入并渲染前端记录
    '''
    if account_amount and account_type:
        children.append(dbc.Row(
            dbc.Col(
                '【{}】类开销【{}】元'.format(account_type, account_amount)
            ),
            # 以字典形式定义id
            id={'type': 'single-account_record', 'index': children.__len__()}
        ))

        return children


@app.callback(
    [Output('account-record-sum', 'children'),
     Output('raw-json', 'children')],
    Input({'type': 'single-account_record', 'index': ALL}, 'children'),
    prevent_initial_call=True
)
def refresh_account_sum(children):
    '''
    对多部件集合single-account_record下所有账目记录进行求和
    '''
    return '账本总开销：{}'.format(sum([int(re.findall('\d+',
                                                 child['props']['children'])[0])
                                  for child in children])), json.dumps(children, indent=2)

if __name__ == '__main__':
    app.run_server(debug=True)