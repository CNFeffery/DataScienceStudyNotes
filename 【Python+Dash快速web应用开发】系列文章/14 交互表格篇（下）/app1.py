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
            style_table={
                'height': '500px',
                'overflow-y': 'auto'
            },
            sort_action='native'
        )
    ],
    style={
        'margin-top': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)