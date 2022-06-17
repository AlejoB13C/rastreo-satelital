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

app = Dash(__name__, assets_url_path='./assets', external_stylesheets=[url_theme1, dbc_css], plugins=[dl.plugins.pages])
app.title = 'Tiempos de viaje'
app.layout = html.Div(
    [
        html.Div(page_title.title, className="p-4 mb-2", style={"margin": "10px"}),
        # html.Div(
        #     [
        #         html.Div(
        #             dcc.Link(f"{page['name']} - {page['path']}", href=page["path"])
        #         )
        #         for page in dash.page_registry.values()
        #         if page["module"] != "pages.not_found_404"
        #     ]
        # ),
        dl.plugins.page_container,
    ],
    style={"padding": "0px", "background-color": main_blue}
)


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)