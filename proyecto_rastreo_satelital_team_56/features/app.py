import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from plotly import express as px

#Import Data
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
days = pd.DataFrame({"Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "Value":[1,2,3,4,5,6,7]})
hours = pd.DataFrame({"Hours":[x for x in range(24)], "Value":[x for x in range(24)]})

#set the mapplot
fig = px.line_mapbox(us_cities, lat="lat", lon="lon", zoom=12)
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0})

#set the daysplot
fig2 = px.bar(days, x="Day", y="Value", color="Value")

#set the hoursplot
fig3 = px.bar(hours, x="Hours", y="Value", color="Value")

# Create the app
app = Dash(__name__, assets_url_path='./assets', external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Tiempos de viaje'

# Layout
sidebar = dbc.Card([
    dbc.Row([
        dbc.Col([
            dcc.Textarea(className='address-input',placeholder='Direccion de origen'),
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Textarea(className='address-input',placeholder='Direccion de destino'),
        ]),
    ]),
    dbc.Row(
        html.Button(id="nclicks-1__button", n_clicks=0, children="Estimar")
    ),
], body=True, )

plots_bottom = dbc.Row([
    dbc.Col([
        html.Div([
            dcc.Graph(id='days__plot', figure=fig2)
        ])
    ]),
    dbc.Col([
        html.Div([
            dcc.Graph(id='hours__plot', figure=fig3)
        ])
    ]),
])

app.layout = dbc.Container([
    html.H1('Tiempos de viaje'),
    html.Hr(),
    html.P('Este dashboard muestra el tiempo de viaje de una ciudad a otra.'),
    dbc.Row([
        dbc.Col([sidebar]),
        dbc.Col([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='map-plot', figure=fig),
                    ]),
                ]),
            ], className='map-container'),
        ], width={'size': 8, 'order': 2}),
    ]),
    plots_bottom,
], fluid=True, style={"background-color": "#f5f5f5"})

# Callbacks
# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8051", debug=True)