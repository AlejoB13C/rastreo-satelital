import pandas as pd

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
days = pd.DataFrame({"Day":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "Value":[1,2,3,4,5,6,7]})
hours = pd.DataFrame({"Hours":[x for x in range(24)], "Value":[x for x in range(24)]})
data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]