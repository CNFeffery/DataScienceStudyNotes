import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output

import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
df.insert(0, '#', df.index)

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dash_table.DataTable(
            id='dash-table',
            data=df.to_dict('records'),
            columns=[
                {'name': column, 'id': column}
                for column in df.columns
            ],
            fixed_rows={'headers': True},
            page_size=15,
            editable=True,
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
        html.H4('与原表格内容比较：', style={'margin-top': '50px'}),
        dcc.Markdown(
            '无差别',
            id='markdown',
            dangerously_allow_html=True
        )
    ],
    style={
        'margin-top': '50px'
    }
)


@app.callback(
    Output('markdown', 'children'),
    Input('dash-table', 'data'),
    prevent_initial_call=True
)
def compare_difference(dash_table_data):
    print(pd.DataFrame(dash_table_data))

    return df.compare(pd.DataFrame(dash_table_data)).to_html()


if __name__ == '__main__':
    app.run_server(debug=True)