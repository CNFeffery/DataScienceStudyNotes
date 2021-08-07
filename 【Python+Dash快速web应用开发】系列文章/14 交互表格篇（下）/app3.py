import dash
import dash_table
import dash_bootstrap_components as dbc

import seaborn as sns

df = sns.load_dataset('iris')

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': column, 'id': column}
                for column in df.columns
            ],
            # 自定义条件筛选单元格样式
            style_filter={
                'background-color': '#e3f2fd'
            },
            style_table={
                'height': '500px',
                'overflow-y': 'auto'
            },
            style_header={
                'font-family': 'Times New Romer',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Romer',
                'text-align': 'center'
            },
            filter_action="native",
            fixed_rows={'headers': True}
        )
    ],
    style={
        'margin-top': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)