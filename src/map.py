import pandas as pd
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster




def mapeo (x, y, z, m, q):
    map_cel = x [x ['name']== 'CollegeClickTV']
    list_map_cel = map_cel ['comp_near'].tolist()

    c= z.find({'name' : {'$in': list_map_cel[0]}})
    c=list(c)
    h = pd.DataFrame(c)
    h

    for i,row in h.iterrows():



        distrito = {
            "location" : [row['location']['coordinates'][1], row['location']['coordinates'][0]],
            "tooltip" : row["name"]
        }


        icon = Icon( color = y,
                    prefix = "fa",
                    icon = q,
                    icon_color = "black")


        Marker (**distrito,icon = icon).add_to(m)
    return m

def Create_map (x, y):
    return folium.Map(location = [x,y], zoom_start = 15, control_scale=True)


def add_market (x, y, q, z):
    for i,row in pd.DataFrame(y).iterrows():

        parque = Marker(location=[row['location']['coordinates'][1],row['location']['coordinates'][0]], tooltip = row['name'], icon = Icon(                     color = z,
                    prefix = "fa",
                    icon = q,
                    icon_color = "black"))
        parque.add_to(x)
    

    return x

def create_data_School(x, y, z):
    g = x[x.name==y]
    list_g = g['comp_near'].tolist()
    list_g
    f = z.find({'name': {'$in': list_g[0]}})
    dt=pd.DataFrame(f)
    lat=[]
    lnt= []
    for i,row in dt.iterrows():
        lat.append(row['location']['coordinates'][1])
        lnt.append(row['location']['coordinates'][0])
    dt.insert(4,'lat', lat)
    dt.insert(5,'lnt', lnt)
    return dt


def Mapa_calor_School (x,y,z):
    for i in y:
        School = x[x.type==i]
        group = folium.FeatureGroup (name = i)
        HeatMap(data = School[["lat","lnt"]], radius = 15).add_to(group)
        group.add_to(z)
    folium.LayerControl(collapsed = False).add_to(z)
    return z
