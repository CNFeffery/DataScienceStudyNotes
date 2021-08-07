import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

from models.age import Age

age_data = (
    pd.DataFrame(Age.fetch_all()).rename(columns={
        'region': '地区',
        'prop_0_to_14': '0到14岁人口占比',
        'prop_15_59': '15到59岁人口占比',
        'prop_60_above': '60岁以上人口占比',
        'prop_65_above': '65岁以上人口占比'
    })
)

fig = px.bar(age_data.melt(id_vars=['地区'],
                           value_vars=['0到14岁人口占比', '15到59岁人口占比', '60岁以上人口占比'],
                           var_name='年龄段',
                           value_name='占比(%)'),
             y="地区", x="占比(%)", color="年龄段", title="七普各地区人口年龄结构",
             color_discrete_map={
                 '0到14岁人口占比': '#0868ac',
                 '15到59岁人口占比': '#43a2ca',
                 '60岁以上人口占比': '#a8ddb5'
             },
             orientation='h')

fig.update_layout(
    font=dict(
        family="Times New Roman, SimSun"
    )
)
fig.update_layout(xaxis_range=[0, 100])

fig.update_layout(
    margin=dict(t=50, b=10)
)

age_page = html.Div(
    [
        html.Div(
            dbc.Table.from_dataframe(age_data, striped=True),
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
