import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

import seaborn as sns

app = dash.Dash(__name__)

# 载入演示数据集
df = sns.load_dataset('iris')
# 创建行下标列
df.insert(loc=0, column='#', value=df.index)

app.layout = html.Div(
    dbc.Container(
        [
            dash_table.DataTable(
                columns=[{'name': column, 'id': column} for column in df.columns],
                data=df.to_dict('records'),
                virtualization=True,
                style_table={
                    'height': '300px'
                },
                style_cell={
                    'background-color': '#fff9c4',
                    'font-family': 'Times New Romer',
                    'text-align': 'center'
                }
            ),
            html.Hr(),
            dash_table.DataTable(
                columns=[{'name': column, 'id': column} for column in df.columns],
                data=df.to_dict('records'),
                virtualization=True,
                style_table={
                    'height': '300px'
                },
                style_header={
                    'background-color': '#b3e5fc',
                    'font-family': 'Times New Romer',
                    'font-weight': 'bold',
                    'font-size': '17px',
                    'text-align': 'left'
                },
                style_data={
                    'font-family': 'Times New Romer',
                    'text-align': 'left'
                }
            )
        ],
        style={
            'margin-top': '100px'
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)