import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from plotly import express as px

#Import Data
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

#set the mapplot
fig = px.line_mapbox(us_cities, lat="lat", lon="lon", zoom=12)
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0})

# Create the app
app = Dash(__name__, assets_url_path='./assets',)
app.title = 'Tiempos de viaje'

# Layout
app.layout = dbc.Container([
    dbc.Row([
        html.H1("Rastreo Satelital", id="ds4a__title", className="h-50 p-1 bg-light borderrounded-3"),
        html.P("Tiempo de viaje: Aqui se inserta una breve descripcióndel aplicativo..."),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.P("Seleccione el día a simular:")
                ]),
                dbc.Row([
                    html.Div([
                        dcc.Dropdown(id="demo__dropdown", options=['Lunes', 'Martes', 'Miercoles'], value='Lunes'),
                    ],id="dd-output__container")
                ]),
                html.P("Seleccione la hora de salida:"),
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='demo-dropdown2', options=['00', '01', '02'], value='00')
                        ], id='dd-output__container_2')
                    ]),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='demo-dropdown3', options=['00', '10', '20'], value='00')
                        ], id='dd-output__container_3')
                    ]),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(id='demo-dropdown4', options=['am', 'pm'], value='am')
                        ],id='dd-output-container4')
                    ]),
                ]),
                dbc.Row([
                    html.P("Indique el origen y el destino"),
                    dbc.Row([
                        html.Div([
                            dcc.Textarea(id='textarea-state-example',value='Input: Direccion de origen',style={'width': '100%', 'height':40})
                        ])
                    ]),
                    dbc.Row([
                        html.Div([
                            dcc.Textarea(id='textarea-state-example2',value='Input: Direccion de destino',style={'width': '100%', 'height':40})
                        ])
                    ])
                ]),
                dbc.Row(
                    html.Button(id="nclicks-1__button", n_clicks=0, children="Estimar")
                ),
                dbc.Row(
                    dbc.Col([
                        html.P("La hora estimada de llegada es: "),
                        html.Div([
                            dcc.Textarea(id='textarea-state-example3',value='Output: Hora de llegada',style={'width': '100%', 'height':40})
                        ])
                    ])
                )
            ])
        ]),
        dbc.Col(
            dcc.Graph(figure=fig)
        )
    ])
])

# app.layout = dbc.Container([dbc.Row([html.H1('Rastreo Satelital',id="ds4a-title", className="h-50 p-1 bg-light borderrounded-3"),
# html.Div(children='''Tiempo de viaje: Aqui se inserta una breve descripcióndel aplicativo...''')]),
# dbc.Row([
# dbc.Col([
# dbc.Row('Seleccione el día a simular.'),
# dbc.Row(html.Div([dcc.Dropdown(options=['Lunes', 'Martes', 'Miercoles'],
# value='Lunes', id='demo-dropdown'), html.Div(id='dd-output-container'),])),
# dbc.Row('\n'),
# dbc.Row('Seleccione la hora de salida'),
# # dbc.Row([
# dbc.Col(html.Div([dcc.Dropdown(options=['00', '01', '02'], value='00',
# id='demo-dropdown2'), html.Div(id='dd-output-container2'),])),
# dbc.Col(html.Div([dcc.Dropdown(options=['00', '10', '20'],value='00',
# id='demo-dropdown3'), html.Div(id='dd-output-container3'),])),
# dbc.Col(html.Div([dcc.Dropdown(options=['am', 'pm'], value='am', id='demo-dropdown4'), html.Div(id='dd-output-container4'),]))
# ]),
# dbc.Row('Indique el origen y el destino'),
# dbc.Row(html.Div([dcc.Textarea(id='textarea-state-example',value='Input: Direccion de origen',style={'width': '100%', 'height':
# 40},)])),
# dbc.Row(html.Div([dcc.Textarea(id='textarea-state-example2',value='Input: Direccion de destino',style={'width': '100%', 'height':
# 40},)])),
# dbc.Row(html.Button('Estimar', id='btn-nclicks-1', n_clicks=0)),
# dbc.Row(dbc.Col(['La hora estimada de llegada es: ',
# html.Div([dcc.Textarea(id='textarea-state-example3',value='Output: Hora de llegada',style={'width': '100%', 'height':40})])
# ])),
# ], md=3),
# dbc.Col(dcc.Graph(figure=fig))
# ])
# ])
# Callbacks
# Start the server
if __name__ == '__main__':
    print('hola')
    app.run_server(host="0.0.0.0", port="8050", debug=True)