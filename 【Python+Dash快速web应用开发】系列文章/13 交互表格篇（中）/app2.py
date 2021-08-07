import dash
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output

import seaborn as sns
import pandas as pd
from tqdm import tqdm

# 压力测试
df = pd.concat([sns.load_dataset('tips') for _ in tqdm(range(1000))], ignore_index=True)
df.insert(0, '#', df.index)

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dbc.Spinner(
            dash_table.DataTable(
                id='dash-table',
                columns=[
                    {'name': column, 'id': column}
                    for column in df.columns
                ],
                page_size=15,  # 设置单页显示15行记录行数
                page_action='custom',
                page_current=0,
                style_header={
                    'font-family': 'Times New Roman',
                    'font-weight': 'bold',
                    'text-align': 'center'
                },
                style_data={
                    'font-family': 'Times New Roman',
                    'text-align': 'center'
                }
            )
        )
    ],
    style={
        'margin-top': '50px'
    }
)


@app.callback(
    [Output('dash-table', 'data'),
     Output('dash-table', 'page_count')],
    [Input('dash-table', 'page_current'),
     Input('dash-table', 'page_size')]
)
def refresh_page_data(page_current, page_size):
    return df.iloc[page_current * page_size:(page_current + 1) * page_size].to_dict('records'), 1 + df.shape[
        0] // page_size


if __name__ == '__main__':
    app.run_server(debug=True)