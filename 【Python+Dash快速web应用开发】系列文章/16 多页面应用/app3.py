import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = dbc.Container(
    [
        html.Div(id='redirect-url-container'),

        dbc.Button('跳转到页面A', id='jump-to-pageA', style={'marginRight': '10px'}),

        dbc.Button('跳转到页面B', id='jump-to-pageB'),
    ],
    style={
        'paddingTop': '100px'
    }
)


@app.callback(
    Output('redirect-url-container', 'children'),
    [Input('jump-to-pageA', 'n_clicks'),
     Input('jump-to-pageB', 'n_clicks')],
)
def jump_to_target(a_n_clicks, b_n_clicks):
    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'] == 'jump-to-pageA.n_clicks':
        return dcc.Location(id='redirect-url', href='/pageA')

    elif ctx.triggered[0]['prop_id'] == 'jump-to-pageB.n_clicks':
        return dcc.Location(id='redirect-url', href='/pageB')

    return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
