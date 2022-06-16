import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from plotly import express as px
from dotenv import load_dotenv
import os

map_token = os.getenv("MAPBOX_API_TOKEN")
map_style = os.getenv("MAP_STYLE")
load_dotenv("../../.env")

#Import Data
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
days = pd.DataFrame({"Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "Value":[1,2,3,4,5,6,7]})
hours = pd.DataFrame({"Hours":[x for x in range(24)], "Value":[x for x in range(24)]})

#set the mapplot
fig = px.line_mapbox(us_cities, lat="lat", lon="lon", zoom=12)
<<<<<<< HEAD
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=10, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0})
=======
fig.update_layout(mapbox_zoom=10, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0},
    mapbox= dict(
        accesstoken = map_token,
        style = map_style
    )
)
>>>>>>> fronted/styles

#set the daysplot
data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
fig2 = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
               )
fig2.update_layout({
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    "font_color": "lightgrey",
})

#set the hoursplot
fig3 = px.bar(hours, x="Hours", y="Value", color="Value")

fig3.update_layout({
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    "font_color": "lightgrey",
})

# Create the app
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)
app = Dash(__name__, assets_url_path='./assets', external_stylesheets=[url_theme1, dbc_css])

app.title = 'Tiempos de viaje'

main_blue= "#162f41"
secondary_blue= "#2c3e50"

# Layout
def address__input(text):
    return html.Div([
        dbc.Label(f"{text}", html_for=f"direccion-{text}__input"),
        dbc.Col([
            dbc.Input(
                id=f"direccion-{text}__input",
                type="text",
                placeholder=f"dirección de {text}"
            ),
        ], width=12)
    ])

sidebar = dbc.Card([
<<<<<<< HEAD
    address__input("origen"),
    address__input("destino"),
    dbc.Row(
        dbc.Col(
            dbc.Button("Estimar", color="primary"),
            width=3
        ),
        align="baseline",
        justify="end",
        style={"margin-top": "10px",
               "margin-right": "10px"}
    )
])

titulo = [html.H1('Tiempos de viaje'),
    html.Hr(),
    html.P('Este dashboard muestra el tiempo de viaje de una ciudad a otra.')]
=======
    html.Div(
        [
            address__input("origen"),
        ]),
    html.Div(
        [
            address__input("destino"),
        ]),
    
    html.Div(
        [
        html.Br(),
        html.P('Range Slider', style={
            'textAlign': 'center'
        }),
        dcc.RangeSlider(
            id='range_slider',
            min=0,
            max=20,
            step=0.5,
            value=[5, 15]
        ),
        ]
    ),
    html.Div(
        [
            dbc.Card(
                [dbc.Checklist(
                    id='check_list',
                    options=[{
                        'label': 'Value One',
                        'value': 'value1'
                    },
                        {
                            'label': 'Value Two',
                            'value': 'value2'
                        },
                        {
                            'label': 'Value Three',
                            'value': 'value3'
                        }
                    ],
                    )
                 ]),
        ]
    ),
    html.Div(
        [
            dbc.Button("Estimar", outline=True, color="primary", className="me-1")
        ]),
    
],body=True, style={"font_color":"white"}
)

titulo = [
    html.H3('Tiempos de viaje', className="bg-primary text-white p-4 mb-2"),
    html.Hr(style={"color": "#FFFFFF"}),
    html.H6('Este dashboard muestra el tiempo de viaje de una ciudad a otra.', className="p-4 mb-2 text-white", style={"background-color": secondary_blue}),
    ]
>>>>>>> fronted/styles

mapa =html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='map-plot', figure=fig),
        ]),
    ]),
], className='map-container')

plots_bottom = dbc.Row([
    dbc.Col([
        html.Div(
            dcc.Graph(id='days__plot', figure=fig2, className="m-4")
        )
    ],md=5),
    dbc.Col([
        html.Div([
            dcc.Graph(id='hours__plot', figure=fig3, className="m-4")
        ])
    ],md=5),
])

<<<<<<< HEAD
app.layout = dbc.Container([
    *titulo,
    dbc.Row([
        dbc.Col(sidebar,width=2),
        dbc.Col([
            dbc.Row(mapa), 
            dbc.Row(plots_bottom)], 
            width={'size': 8, 'order': 2}),
    ]),
], fluid=True, style={"background-color": "#f5f5f5"})
=======
app.layout = dbc.Container(
        [    
            html.Div(titulo, className="p-4 mb-2", style={"margin": "10px"}),
            dbc.Row(
                [
                    dbc.Col(sidebar, md=2, style={'background-color': main_blue}),
                    dbc.Col(
                        [                                
                            dbc.Row(mapa),   
                            dbc.Row(plots_bottom)
                        ], md=10, style={'background-color': main_blue}
                    )
                ],
            )
        ],
    className="dbc",
    fluid=True,
    style={"padding": "0px", "background-color": main_blue}
)
>>>>>>> fronted/styles

# Callbacks
# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8051", debug=True)