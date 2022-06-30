from dash import Dash, html, dcc
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from proyecto_rastreo_satelital_team_56.components import page_title

main_blue= "#162f41"
secondary_blue= "#2c3e50"

# Create the app
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)

app = Dash(
    __name__,
    assets_url_path='./assets',
    external_stylesheets=[url_theme1, dbc_css],
    plugins=[dl.plugins.pages],
    suppress_callback_exceptions=True,
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0'}]
    )

server = app.server