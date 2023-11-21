import dash
import numpy as np
from dash import html, Patch
import feffery_maplibre as fm
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdSelect(
                    id='font-select',
                    options=[
                        {
                            'label': font,
                            'value': font
                        }
                        for font in [
                            'LXGW WenKai Regular',
                            'DingTalk JinBuTi Regular',
                            'LXGW Neo XiHei Regular',
                            'XiaoLaiSC Regular'
                        ]
                    ],
                    value='LXGW WenKai Regular',
                    allowClear=False,
                    style={
                        'width': 200
                    }
                )
            ],
            style={
                'position': 'absolute',
                'top': 20,
                'left': 20,
                'zIndex': 999
            }
        ),
        fm.MapContainer(
            [
                fm.NavigationControl(
                    visualizePitch=True
                ),

                # 调用esri开放影像底图
                fm.Source(
                    [
                        fm.Layer(
                            id='img-layer',
                            layerProps={
                                'type': 'raster',
                                'source': 'img-source'
                            }
                        )
                    ],
                    id='img-source',
                    sourceProps={
                        'type': 'raster',
                        'tiles': [
                            'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        ],
                        'tileSize': 256
                    }
                ),

                # 点要素示例
                fm.Source(
                    [
                        fm.Layer(
                            id='point-layer',
                            layerProps={
                                'type': 'circle',
                                'layout': {},
                                'paint': {
                                    'circle-color': 'white',
                                    'circle-radius': 5
                                }
                            }
                        ),
                        fm.Layer(
                            id='point-text-layer',
                            layerProps={
                                'type': 'symbol',
                                'layout': {
                                    'text-field': '{字段1}\n{字段2}',
                                    'text-size': 18,
                                    'text-font': [],
                                    'text-allow-overlap': True
                                },
                                'paint': {
                                    'text-color': 'white',
                                    'text-halo-color': '#000000',
                                    'text-halo-width': 3
                                }
                            }
                        )
                    ],
                    id='point-source',
                    sourceProps={
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [
                                {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Point',
                                        'coordinates': [-5, 0]
                                    },
                                    'properties': {
                                        '字段1': '落霞与孤鹜齐飞',
                                        '字段2': '秋水共长天一色'
                                    }
                                }
                            ]
                        }
                    }
                ),

                # 线要素示例
                fm.Source(
                    [
                        fm.Layer(
                            id='line-layer',
                            layerProps={
                                'type': 'line',
                                'layout': {},
                                'paint': {
                                    'line-color': 'white',
                                    'line-width': 3
                                }
                            }
                        ),
                        fm.Layer(
                            id='line-text-layer',
                            layerProps={
                                'type': 'symbol',
                                'layout': {
                                    'text-field': '{字段1} {字段2}',
                                    'text-size': 18,
                                    'text-font': [],
                                    'symbol-placement': 'line',
                                    'symbol-spacing': 10
                                },
                                'paint': {
                                    'text-color': 'white',
                                    'text-halo-color': '#000000',
                                    'text-halo-width': 3
                                }
                            }
                        )
                    ],
                    id='line-source',
                    sourceProps={
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [
                                {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'LineString',
                                        'coordinates': [
                                            [
                                                i,
                                                np.sin(i)
                                            ]
                                            for i in np.arange(0, 10, 0.1)
                                        ]
                                    },
                                    'properties': {
                                        '字段1': '落霞与孤鹜齐飞',
                                        '字段2': '秋水共长天一色'
                                    }
                                }
                            ]
                        }
                    }
                ),

                # 面要素示例
                fm.Source(
                    [
                        fm.Layer(
                            id='polygon-layer',
                            layerProps={
                                'type': 'fill',
                                'layout': {},
                                'paint': {
                                    'fill-color': '#f5f5f5',
                                    'fill-opacity': 0.5
                                }
                            }
                        ),
                        fm.Layer(
                            id='polygon-text-layer',
                            layerProps={
                                'type': 'symbol',
                                'layout': {
                                    'text-field': '{字段1} {字段2}',
                                    'text-size': 18,
                                    'text-font': [],
                                    'symbol-spacing': 75
                                },
                                'paint': {
                                    'text-color': 'white',
                                    'text-halo-color': '#000000',
                                    'text-halo-width': 3
                                }
                            }
                        )
                    ],
                    id='polygon-source',
                    sourceProps={
                        'type': 'geojson',
                        'data': {
                            'type': 'FeatureCollection',
                            'features': [
                                {
                                    'type': 'Feature',
                                    'geometry': {
                                        'type': 'Polygon',
                                        'coordinates': [
                                            [
                                                [-4, -2],
                                                [-4, -4],
                                                [-2, -4],
                                                [-2, -2],
                                                [-4, -2]
                                            ]
                                        ]
                                    },
                                    'properties': {
                                        '字段1': '落霞与孤鹜齐飞',
                                        '字段2': '秋水共长天一色'
                                    }
                                }
                            ]
                        }
                    }
                )
            ],
            initialViewState={
                'zoom': 6,
                'longitude': 2
            },
            style={
                'height': '100%',
                'position': 'absolute'
            },
            mapStyle={
                'version': 8,
                'sources': {},
                'layers': [],
                'glyphs': 'http://127.0.0.1:3000/font/{fontstack}/{range}'
            }
        )
    ],
    style={
        'height': '100vh',
        'position': 'relative'
    }
)


@app.callback(
    [Output('point-text-layer', 'layerProps'),
     Output('line-text-layer', 'layerProps'),
     Output('polygon-text-layer', 'layerProps')],
    Input('font-select', 'value')
)
def update_font(value):

    p = Patch()
    p['layout']['text-font'] = [value]

    return [p] * 3


if __name__ == '__main__':
    app.run(debug=False)
