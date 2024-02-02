import dash
import random
import requests
from dash import html
import feffery_maplibre as fm

app = dash.Dash(__name__)

# 获取全部图标名称
all_icons = list(
    requests
    .get(
        'http://127.0.0.1:3000/sprite/设施点.json'
    )
    .json()
    .keys()
)

app.layout = html.Div(
    [
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),

                fm.SourceGroup(
                    [
                        # 基础底图示例
                        fm.Source(
                            [
                                fm.Layer(
                                    id='base-map-layer',
                                    layerProps={
                                        'type': 'raster',
                                        'source': 'base-map-source'
                                    }
                                )
                            ],
                            id='base-map-source',
                            sourceProps={
                                'type': 'raster',
                                'tiles': [
                                    'https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
                                ],
                                'tileSize': 256
                            }
                        ),
                        # 示例点要素图层
                        fm.Source(
                            fm.Layer(
                                id='demo-points-layer',
                                layerProps={
                                    'type': 'symbol',
                                    'source': 'demo-points-source',
                                    'layout': {
                                        'icon-image': '{图标}',
                                        'icon-size': 0.5,
                                        'icon-allow-overlap': True
                                    }
                                }
                            ),
                            id='demo-points-source',
                            sourceProps={
                                'type': 'geojson',
                                'data': {
                                    'type': 'FeatureCollection',
                                    'features': [
                                        {
                                            'type': 'Feature',
                                            'geometry': {
                                                'type': 'Point',
                                                'coordinates': [
                                                    random.normalvariate(
                                                        107.252575, 0.5),
                                                    random.normalvariate(
                                                        29.607626, 0.5)
                                                ]
                                            },
                                            'properties': {
                                                '图标': random.choice(all_icons)
                                            }
                                        }
                                        for i in range(1000)
                                    ]
                                }
                            }
                        )
                    ]
                )
            ],
            mapStyle={
                'version': 8,
                'sprite': 'http://127.0.0.1:3000/sprite/设施点',
                'sources': {},
                'layers': []
            },
            initialViewState={
                "longitude": 107.252575,
                "latitude": 29.607626,
                "zoom": 6,
                "pitch": 0,
                "bearing": 0
            },
            maxZoom=9,
            style={
                'height': '100%'
            }
        )
    ],
    style={
        'height': '100vh'
    }
)

if __name__ == '__main__':
    app.run()
