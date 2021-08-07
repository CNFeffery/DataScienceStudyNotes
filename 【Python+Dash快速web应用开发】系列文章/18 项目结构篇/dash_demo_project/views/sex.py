import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

from models.sex import Sex

sex_data = (
    pd.DataFrame(Sex.fetch_all()).rename(columns={
        'region': '地区',
        'male': '男性占比',
        'female': '女性占比'
    })
    .sort_values('男性占比')
)

fig = px.bar(sex_data.melt(id_vars=['地区'],
                           value_vars=['男性占比', '女性占比'],
                           var_name='性别',
                           value_name='占比(%)'),
             y="地区", x="占比(%)", color="性别", title="七普各地区人口性别结构",
             color_discrete_map={
                 '男性占比': '#60a5fa',
                 '女性占比': '#f472b6'
             },
             orientation='h')

fig.add_vline(x=50, line_width=2, line_dash="dash", line_color="#616161")

fig.update_layout(
    font=dict(
        family="Times New Roman, SimSun"
    )
)
fig.update_layout(xaxis_range=[0, 100])

fig.update_layout(
    margin=dict(t=50, b=10)
)

sex_page = html.Div(
    [
        html.Div(
            dbc.Table.from_dataframe(sex_data, striped=True),
            style={
                'overflowY': 'auto',
                'flex': '1'
            }
        ),
        html.Div(
            dcc.Graph(figure=fig, style={'height': '100%'}),
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
