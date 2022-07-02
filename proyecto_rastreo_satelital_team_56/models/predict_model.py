import osmnx as ox
import pandas as pd
import numpy as np
import connectorx as cx
import folium
from IPython.display import HTML, display

place = "Bogota, Colombia"
G = ox.graph_from_place(place, network_type="drive")

def GetBestRoute(orig:tuple, dest:tuple,weight='length'):
    """
    Resturns the best route depending on the
    weight, if it is ecqual to lenght the function
    minimizes the distance in orther to get the
    best route.
    
    Args:
        orig (tuple): (lat,lon) of origin
        dest (tuple): (lat,lon) of destination
        weight (str, optional): minimizing parameter. Defaults to 'length'.
    """
    orign = ox.distance.nearest_nodes(G,orig[1],orig[0])
    destn = ox.distance.nearest_nodes(G,dest[1],dest[0])
    print(orign,destn)
    route = ox.distance.shortest_path(G, orign, destn, weight=weight)
    return route

def ComputeEdgesFromRoute(route:list):
    Edges = []
    for i in range(len(route)-1):
        Edges.append((route[i],route[i+1],0))
    return Edges





route = GetBestRoute((4.635507,-74.072870),(4.643917,-74.082635))
print(route)
ComputeEdgesFromRoute(route)