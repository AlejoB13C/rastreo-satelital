from dash import html

main_blue= "#162f41"
secondary_blue= "#2c3e50"


title = [
    html.H3('Tiempos de viaje', className="bg-primary text-white p-4 mb-2"),
    html.Hr(style={"color": "#FFFFFF"}),
    html.H6('Este dashboard muestra el tiempo de viaje de una ciudad a otra.', className="p-4 mb-2 text-white", style={"background-color": secondary_blue}),
    ]