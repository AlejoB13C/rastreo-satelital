from plotly import express as px
from proyecto_rastreo_satelital_team_56.data import import_temp_data


hours = import_temp_data.hours
hoursplot = px.bar(hours, x="Hours", y="Value", color="Value")

hoursplot.update_layout({
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    "font_color": "lightgrey",
})