import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from callbacks.statistics import statistics_data

statistics_page = html.Div(
    [
        html.Div(
            dbc.Table.from_dataframe(statistics_data, striped=True),
            style={
                'overflowY': 'auto',
                'flex': '1'
            }
        ),
        html.Div(
            [
                dbc.RadioItems(
                    options=[
                        {'label': '六普vs七普比例变化', 'value': '六普vs七普比例变化'},
                        {'label': '七普人口', 'value': '七普人口'}
                    ],
                    id='statistics-chart-switch',
                    value='六普vs七普比例变化',
                    style={
                        'position': 'fixed',
                        'right': '20px',
                        'top': '20px',
                        'zIndex': '999'
                    },
                    inline=True
                ),
                dcc.Graph(
                    id='statistics-chart',
                    style={'height': '100%'},
                    config={'displayModeBar': False}
                )
            ],
            style={
                'flex': '1',
                'height': '100%'
            }
        )
    ],
    style={
        'display': 'flex',
        'height': '100%'
    }
)
