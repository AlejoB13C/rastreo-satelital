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
    brand="Travel Times",
    color="primary",
    dark=True,
    className="mb-2 h-10",
)

app.title = 'Tiempos de viaje'
app.layout =  dbc.Container(
    [
        navbar,
        # html.Div(page_title.title, className="p-4 mb-2", style={"margin": "10px"}),
        dl.plugins.page_container,
    ],
    style={"padding": "0px", "background-color": main_blue, "margin": "0px", "height": "100vh"},
    className="dbc h-100",
    fluid=True,
)

if __name__ == "__main__":
   server.run(debug=False, port=8050)