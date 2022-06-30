import os
from pyprojroot import here
from dotenv import load_dotenv
from plotly import express as px
from proyecto_rastreo_satelital_team_56.data import import_temp_data

dotenv_path = here().joinpath(".env")
load_dotenv(dotenv_path)

us_cities = import_temp_data.us_cities

map_token = os.getenv("MAPBOX_API_TOKEN")
map_style = os.getenv("MAP_STYLE")

#set the mapplot
map_plot = px.line_mapbox(us_cities, lat="lat", lon="lon", zoom=12)
map_plot.update_layout(mapbox_zoom=10, mapbox_center_lat= 4.65,
    mapbox_center_lon= -74.1, margin={"r":0,"t":0,"l":0,"b":0},
    mapbox= dict(
        accesstoken = map_token,
        style = map_style
    ),
    # height=720
)