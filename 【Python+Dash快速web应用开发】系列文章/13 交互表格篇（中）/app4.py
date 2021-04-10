import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:mysql@localhost/DASH')

app = dash.Dash(__name__)

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
                'font-family': 'Times New Romer',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Romer',
                'text-align': 'center'
            },
            style_data_conditional=[
                {
                    # 对选中状态下的单元格进行自定义样式
                    "if": {"state": "selected"},
                    "background-color": "#b3e5fc",
                    "border": "none"
                },
            ]
        ),
        dbc.Button('同步变动到数据库', id='update-tables', style={'display': 'none'}),
        html.P(id='message')
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
     Output('dash-table', 'columns'),
     Output('update-tables', 'style')],
    Input('table-select', 'value')
)
def render_dash_table(value):
    if value:
        df = pd.read_sql_table(value, con=engine)

        return df.to_dict('records'), [
            {'name': column, 'id': column}
            for column in df.columns
        ], {'margin-top': '25px'}

    else:
        return [], [], {'display': 'none'}


@app.callback(
    [Output('message', 'children'),
     Output('message', 'style')],
    Input('update-tables', 'n_clicks'),
    [State('dash-table', 'data'),
     State('table-select', 'value')]
)
def update_to_database(n_clicks, data, value):

    if n_clicks:

        try:
            pd.DataFrame(data).to_sql(value, con=engine, if_exists='replace', index=False)

            return '更新成功！', {'color': 'green'}
        except Exception as e:
            return f'更新失败！{e}', {'color': 'red'}

    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)