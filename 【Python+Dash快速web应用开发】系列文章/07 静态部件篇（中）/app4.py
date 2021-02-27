import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

fake_df = pd.DataFrame(np.random.rand(1000).reshape(200, 5))
fake_df.rename(lambda s: f'字段{s}', axis=1, inplace=True) # 批量格式化列名

app = dash.Dash(__name__)

app.layout = html.Div(
    dbc.Container(
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [html.Th('行下标', style={'text-align': 'center'})] +
                        [
                            html.Th(column, style={'text-align': 'center'})
                            for column in fake_df.columns
                        ]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [html.Th(f'#{idx}', style={'text-align': 'center'})] +
                            [
                               html.Td(row[column], style={'text-align': 'center'})
                                for column in fake_df.columns
                            ]
                        )
                        for idx, row in fake_df.iterrows()
                    ]
                )
            ],
            striped=True,
            bordered=True
        ),
        style={
            'margin-top': '50px'  # 设置顶部留白区域高度
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)