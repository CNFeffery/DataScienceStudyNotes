import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label('storage = "memory"时'),
                        dbc.Input(id='input-memory1', autoComplete='off'),
                        dbc.Input(id='input-memory2', style={'margin-top': '3px'}),
                        dcc.Store(id='data-in-memory')
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label('storage = "session"时'),
                        dbc.Input(id='input-session1', autoComplete='off'),
                        dbc.Input(id='input-session2', style={'margin-top': '3px'}),
                        dcc.Store(id='data-in-session', storage_type='session')
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label('storage = "local"时'),
                        dbc.Input(id='input-local1', autoComplete='off'),
                        dbc.Input(id='input-local2', style={'margin-top': '3px'}),
                        dcc.Store(id='data-in-local', storage_type='local')
                    ]
                ),
            ]
        )
    ],
    style={
        'margin-top': '100px',
        'max-width': '600px'
    }
)


# memory对应回调
@app.callback(
    Output('data-in-memory', 'data'),
    Input('input-memory1', 'value')
)
def data_in_memory_save_data(value):
    if value:
        return value

    return dash.no_update


@app.callback(
    Output('input-memory2', 'placeholder'),
    Input('data-in-memory', 'data')
)
def data_in_memory_placeholder(data):
    if data:
        return data

    return dash.no_update


# session对应回调
@app.callback(
    Output('data-in-session', 'data'),
    Input('input-session1', 'value')
)
def data_in_session_save_data(value):
    if value:
        return value

    return dash.no_update


@app.callback(
    Output('input-session2', 'placeholder'),
    Input('data-in-session', 'data')
)
def data_in_session_placeholder(data):
    if data:
        return data

    return dash.no_update


# local对应回调
@app.callback(
    Output('data-in-local', 'data'),
    Input('input-local1', 'value')
)
def data_in_local_save_data(value):
    if value:
        return value

    return dash.no_update


@app.callback(
    Output('input-local2', 'placeholder'),
    Input('data-in-local', 'data')
)
def data_in_local_placeholder(data):
    if data:
        return data

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
