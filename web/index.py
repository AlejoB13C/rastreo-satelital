from dash import Dash, html, dcc
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from proyecto_rastreo_satelital_team_56.components import page_title

from app import app, server

main_blue= "#162f41"
secondary_blue= "#2c3e50"

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.title = 'Tiempos de viaje'
app.layout =  dbc.Container(
    [
        navbar,
        html.Div(page_title.title, className="p-4 mb-2", style={"margin": "10px"}),
        # html.Div(
        #     [
        #         html.Div(
        #             dcc.Link(f"{page['name']}", href=page["path"])
        #         )
        #         for page in dash.page_registry.values()
        #         if page["module"] != "pages.not_found_404"
        #     ]
        # ),
        dl.plugins.page_container,
    ],
    style={"padding": "0px", "background-color": main_blue, "margin": "0px"},
    className="dbc",
    fluid=True,
)

if __name__ == "__main__":
   server.run(debug=True, port=8050)