import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
import dash_uploader as du

import re
import os
import pandas as pd
from sqlalchemy import create_engine
import cchardet as chardet

postgres_url = 'postgresql://postgres:CUDLCUDL@localhost:5432/Dash'
engine = create_engine(postgres_url)

app = dash.Dash(__name__)

du.configure_upload(app, 'upload')

app.layout = html.Div(
    dbc.Container(
        [
            du.Upload(
                id='upload',
                filetypes=['csv'],
                text='点击或拖动文件到此进行上传！',
                text_completed='已完成上传文件：',
                cancel_button=True,
                pause_button=True),
            html.Hr(),
            dbc.Form(
                [
                    dbc.FormGroup(
                        [
                            dbc.Label("设置入库表名", html_for="table-name"),
                            dbc.Input(
                                id='table-name',
                                autoComplete='off'
                            ),
                            dbc.FormText(
                                "表名只允许包含大小写字母、下划线或数字，且不能以数字开头，同时请注意表名是否与库中现有表重复！", color="secondary"
                            ),
                            dbc.FormFeedback(
                                "表名合法！", valid=True
                            ),
                            dbc.FormFeedback(
                                "表名不合法！",
                                valid=False,
                            ),
                        ]
                    ),
                    dbc.FormGroup(
                        [
                            dbc.Button('提交入库', id='commit', outline=True)
                        ]
                    )
                ],
                style={
                    'background-color': 'rgba(224, 242, 241, 0.4)'
                }
            ),
            dbc.Spinner(
                [
                    html.P(id='commit-status-message', style={'color': 'red'}),
                    dbc.Label('预览至多前10000行', html_for='uploaded-table'),
                    dash_table.DataTable(
                        id='uploaded-table',
                        style_table={
                            'height': '400px'
                        },
                        virtualization=True,
                        style_as_list_view=True,
                        style_cell={
                            'font-family': 'Times New Romer',
                            'text-align': 'center'
                        },
                        style_header={
                            'font-weight': 'bold'
                        },
                        style_data_conditional=[
                            {
                                'if': {
                                    # 选中行下标为奇数的行
                                    'row_index': 'odd'
                                },
                                'background-color': '#cfd8dc'
                            }
                        ]
                    )
                ]
            )
        ],
        style={
            'margin-top': '30px'
        }
    )
)


@app.callback(
    [Output('table-name', 'invalid'),
     Output('table-name', 'valid')],
    Input('table-name', 'value')
)
def check_table_name(value):
    ''''
    检查表名是否合法
    '''
    if value:

        # 查询库中已存在非系统表名
        exists_table_names = (
            pd
                .read_sql('''SELECT tablename FROM pg_tables''', con=engine)
                .query('~(tablename.str.startswith("pg") or tablename.str.startswith("sql_"))')
        )

        if (re.findall('^[A-Za-z0-9_]+$', value)[0].__len__() == value.__len__()) \
                and not re.findall('^\d', value) \
                and value not in exists_table_names['tablename'].tolist():
            return False, True

        return True, False

    return dash.no_update


@app.callback(
    Output('commit-status-message', 'children'),
    Input('commit', 'n_clicks'),
    [State('table-name', 'valid'),
     State('table-name', 'value'),
     State('upload', 'isCompleted'),
     State('upload', 'fileNames'),
     State('upload', 'upload_id')]
)
def control_table_commit(n_clicks,
                         table_name_valid,
                         table_name,
                         isCompleted,
                         fileNames,
                         upload_id):
    '''
    控制已上传表格的入库
    '''
    if all([n_clicks, table_name_valid, table_name, isCompleted, fileNames, upload_id]):
        uploaded_df = pd.read_csv(os.path.join('upload', upload_id, fileNames[0]),
                                  encoding=chardet.detect(open(os.path.join('upload', upload_id, fileNames[0]),
                                                               'rb').read())['encoding'])

        uploaded_df.to_sql(table_name, con=engine)

        return '入库成功！'

    return dash.no_update


@app.callback(
    [Output('uploaded-table', 'data'),
     Output('uploaded-table', 'columns')],
    Input('upload', 'isCompleted'),
    [State('upload', 'fileNames'),
     State('upload', 'upload_id')]
)
def render_table(isCompleted, fileNames, upload_id):
    '''
    控制预览表格的渲染
    '''
    if isCompleted:
        uploaded_df = pd.read_csv(os.path.join('upload', upload_id, fileNames[0]),
                                  encoding=chardet.detect(open(os.path.join('upload', upload_id, fileNames[0]),
                                                               'rb').read())['encoding']).head(10000)

        uploaded_df.insert(0, '#', range(uploaded_df.shape[0]))

        return uploaded_df.to_dict('record'), [{'name': column, 'id': column} for column in uploaded_df.columns]

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)