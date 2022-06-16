import pandas as pd
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from plotly import express as px
from dotenv import load_dotenv
import os

from dash_labs.plugins import register_page

from proyecto_rastreo_satelital_team_56.components import map_plot, temp_plot1, temp_plot2
from proyecto_rastreo_satelital_team_56.data import import_temp_data


register_page(__name__)

fig = map_plot.map_plot         #Set map plot
fig2 = temp_plot1.daysplot      #set the daysplot
fig3 = temp_plot2.hoursplot     #set the hoursplot

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

def layout():
    return dbc.Container(
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

# # Callbacks
# # Start the server
# if __name__ == '__main__':
#     app.run_server(host="0.0.0.0", port="8051", debug=True)