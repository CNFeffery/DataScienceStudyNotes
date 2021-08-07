import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

from flask import send_from_directory

import os
import uuid
from sqlalchemy import create_engine
import pandas as pd

try:
    os.mkdir("downloads")
except FileExistsError:
    pass

engine = create_engine('mysql+pymysql://root:mysql@localhost/DASH')

app = dash.Dash(__name__)


@app.server.route('/download/<file>')
def download(file):
    return send_from_directory('downloads', file)


app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dbc.Button('更新数据表', id='refresh-tables', style={'width': '100%'}), width=2),
                dbc.Col(dcc.Dropdown(id='table-select', style={'width': '100%'}), width=2)
            ]
        ),
        html.Hr(),
        dash_table.DataTable(
            id='dash-table',
            editable=True,
            page_size=15,
            style_header={
                'font-family': 'Times New Roman',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Roman',
                'text-align': 'center'
            },
            style_data_conditional=[
                {
                    # 对选中状态下的单元格进行自定义样式
                    "if": {"state": "selected"},
                    "background-color": "#b3e5fc",
                    "border": "none"
                },
            ],
            filter_action="native"
        ),
        html.Br(),
        html.A(id='download-url', target="_blank")
    ],
    style={
        'margin-top': '50px'
    }
)


@app.callback(
    Output('table-select', 'options'),
    Input('refresh-tables', 'n_clicks')
)
def refresh_tables(n_clicks):
    if n_clicks:
        return [
            {
                'label': table,
                'value': table
            }
            for table in pd.read_sql_query('SHOW TABLES', con=engine)['Tables_in_dash']
        ]

    return dash.no_update


@app.callback(
    [Output('dash-table', 'data'),
     Output('dash-table', 'columns')],
    Input('table-select', 'value')
)
def render_dash_table(value):
    if value:
        df = pd.read_sql_table(value, con=engine)

        return df.to_dict('records'), [
            {'name': column, 'id': column}
            for column in df.columns
        ]

    else:
        return [], []


@app.callback(
    [Output("download-url", "href"),
     Output("download-url", "children")],
    [Input("dash-table", "derived_virtual_data"),
     Input("dash-table", "filter_query")],
    prevent_initial_call=True
)
def download_table(derived_virtual_data, filter_query):
    if derived_virtual_data:
        print(derived_virtual_data)

        filename = f"output_{uuid.uuid1()}.xlsx"

        pd.DataFrame(derived_virtual_data).to_excel("downloads/" + filename, index=False)

        return "/download/" + filename, "下载当前状态表格"

    return "", ""


if __name__ == '__main__':
    app.run_server(debug=True)