from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from proyecto_rastreo_satelital_team_56.components import map_plot, sidebar


register_page(__name__, name="Map View", path="/")

fig = map_plot.map_plot         #Set map plot

main_blue= "#162f41"
secondary_blue= "#2c3e50"

# Layout
sidebar = sidebar.sidebar

mapa =html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='map-plot', figure=fig, style={'height': '89.5vh'}),
        ]),
    ]),
], className='map-container')

def layout():
    return dbc.Row(
                [
                    dbc.Col(sidebar, md=2, style={'background-color': main_blue, 'height': '100%'}),
                    dbc.Col(
                        [                                
                            dbc.Row(mapa),   
                        ], md=10, style={'background-color': main_blue, 'height': '100%'}
                    )
                ],
                className="map-container h-100"
            )