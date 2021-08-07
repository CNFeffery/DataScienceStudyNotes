from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from models.statistics import Statistics

from server import app

statistics_data = (
    pd.DataFrame(Statistics.fetch_all()).rename(columns={
        'region': '地区',
        'pop_2020': '七普总人口',
        'prop_2020': '七普人口占全国比例',
        'prop_2010': '六普人口占全国比例'
    })
        .query('~地区.str.contains("国")', engine='python')
        .sort_values('七普人口占全国比例')
)


@app.callback(
    Output('statistics-chart', 'figure'),
    Input('statistics-chart-switch', 'value'),
)
def statistics_switch_chart(value):
    if value == '六普vs七普比例变化':
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=statistics_data['地区'],
            x=statistics_data['六普人口占全国比例'],
            name='六普人口占比',
            marker_color='indianred',
            orientation='h'
        ))
        fig.add_trace(go.Bar(
            y=statistics_data['地区'],
            x=statistics_data['七普人口占全国比例'],
            name='七普人口占比',
            marker_color='lightsalmon',
            orientation='h'
        ))

        fig.update_layout(
            font=dict(
                family="Times New Roman, SimSun",
                size=18
            )
        )

        fig.update_layout(
            title_font_family="Times New Roman, SimSun"
        )

        fig.update_layout(
            margin=dict(t=50, b=10)
        )

        return fig

    else:

        fig = px.bar(statistics_data, y='地区', x='七普总人口',
                     color='七普总人口',
                     color_continuous_scale='Reds',
                     orientation='h')

        fig.update_layout(
            margin=dict(t=50, b=10)
        )

        return fig
