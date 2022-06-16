from dash import Dash, html, dcc
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc


# Create the app
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)
app = Dash(__name__, assets_url_path='./assets', external_stylesheets=[url_theme1, dbc_css], plugins=[dl.plugins.pages])

app.title = 'Tiempos de viaje'

dl.plugins.register_page("another_home", layout=html.Div("We're home!"), path="/")
dl.plugins.register_page(
    "very_important", layout=html.Div("Don't miss it!"), path="/important", order=0
)

app.layout = html.Div(
    [
        html.H1("App Frame"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']} - {page['path']}", href=page["path"])
                )
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ]
        ),
        dl.plugins.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)