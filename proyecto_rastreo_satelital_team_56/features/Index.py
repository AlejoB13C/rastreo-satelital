import os
import pandas as pd
import json
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import folium
from folium.plugins import HeatMap
from plotly import express as px

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
fig = px.line_mapbox(us_cities, lat="lat", lon="lon", zoom=12)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
# Create the app
workspace_user = os.getenv('JUPYTERHUB_USER') # Get DS4A Workspace user name
request_path_prefix = None
if workspace_user:
    request_path_prefix = '/user/' + workspace_user + '/proxy/8050/'
app = Dash(__name__, requests_pathname_prefix=request_path_prefix,
external_stylesheets=[dbc.themes.SIMPLEX],
    meta_tags=[{'name':'viewport', 'content':'width=device-width,initial-scale=1.0'}])
app.title = 'Tiempos de viaje'
# Layout
app.layout = dbc.Container([dbc.Row([html.H1('Rastreo Satelital',id="ds4a-title", className="h-50 p-1 bg-light borderrounded-3"),
html.Div(children='''Tiempo de viaje: Aqui se inserta una breve descripcióndel aplicativo...''')]),
dbc.Row([
dbc.Col([
dbc.Row('Seleccione el día a simular.'),
dbc.Row(html.Div([dcc.Dropdown(['Lunes', 'Martes', 'Miercoles'],
'Lunes', id='demo-dropdown'), html.Div(id='dd-output-container'),])),
dbc.Row('\n'),
dbc.Row('Seleccione la hora de salida'),
dbc.Row([
dbc.Col(html.Div([dcc.Dropdown(['00', '01', '02'], '00',
id='demo-dropdown2'), html.Div(id='dd-output-container2'),])),
dbc.Col(html.Div([dcc.Dropdown(['00', '10', '20'], '00',
id='demo-dropdown3'), html.Div(id='dd-output-container3'),])),
dbc.Col(html.Div([dcc.Dropdown(['am', 'pm'], 'am', id='demo-dropdown4'), html.Div(id='dd-output-container4'),]))
]),
dbc.Row('Indique el origen y el destino'),
dbc.Row(html.Div([dcc.Textarea(id='textarea-state-example',value='Input: Direccion de origen',style={'width': '100%', 'height':
40},)])),
dbc.Row(html.Div([dcc.Textarea(id='textarea-state-example2',value='Input: Direccion de destino',style={'width': '100%', 'height':
40},)])),
dbc.Row(html.Button('Estimar', id='btn-nclicks-1', n_clicks=0)),
dbc.Row(dbc.Col(['La hora estimada de llegada es: ',
html.Div([dcc.Textarea(id='textarea-state-example3',value='Output: Hora de llegada',style={'width': '100%', 'height':40})])
])),
], md=3),
dbc.Col(dcc.Graph(figure=fig))
])
])
# Callbacks
# Start the server
if __name__ == '__main__':
    print('hola')
    app.run_server(host="0.0.0.0", port="8050", debug=True)