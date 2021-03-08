import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Tabs(
            [
                dbc.Tab(label='选项卡1', tab_style={'background-color': 'lightgrey'}),
                dbc.Tab(label='选项卡2', label_style={'color': 'red'}),
                dbc.Tab(label='选项卡3',
                        tab_style={'margin-left': 'auto'},
                        active_label_style={'color': 'green'}),
            ]
        ),
        style={'margin-top': '100px'}
    )
)


if __name__ == '__main__':
    app.run_server(debug=True)