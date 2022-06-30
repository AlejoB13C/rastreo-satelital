from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from proyecto_rastreo_satelital_team_56.components import temp_plot1, temp_plot2

register_page(__name__, name="Tendences")

main_blue= "#162f41"
secondary_blue= "#2c3e50"

fig2 = temp_plot1.daysplot      #set the daysplot
fig3 = temp_plot2.hoursplot     #set the hoursplot

plots_bottom = dbc.Row([
    dbc.Col([
        html.Div(
            dcc.Graph(id='days__plot', figure=fig2, className="m-4")
        )
    ],md=6),
    dbc.Col([
        html.Div([
            dcc.Graph(id='hours__plot', figure=fig3, className="m-4")
        ])
    ],md=6),
])

def layout():
    return html.Div(
        [    
            dbc.Row(
                [
                    dbc.Col(
                        [                                
                            dbc.Row(plots_bottom)
                        ], md=12, style={'background-color': main_blue}
                    )
                ],
            )
        ],
    style={"padding": "0px", "background-color": main_blue}
)