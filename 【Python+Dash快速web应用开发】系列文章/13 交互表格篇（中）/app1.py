import dash
import dash_bootstrap_components as dbc
import dash_table

import seaborn as sns

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
            page_size=15,  # 设置单页显示15行记录行数
            style_header={
                'font-family': 'Times New Romer',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Romer',
                'text-align': 'center'
            }
        )
    ],
    style={
        'margin-top': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)