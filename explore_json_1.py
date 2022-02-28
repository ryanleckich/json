import json
from sys import last_traceback

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readbale_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)


list_of_eqs = eq_data["features"]

mags, lons, last = []

for eq in list_of_eqs:
    mag_eg = eq["properties"]["mag"]
    lon = eq["geomeryt"]["coordinates"[0]]
    lat = eq["geomeryt"]["coordinates"[0]]
    mags.append(mags)
    lon.append(lon)
    lat.append(lat)


print(mags[:10])
print(len(list_of_eqs))

from plotly.graph_objs import Sacattergo, layout
from plotly import offline

data = [Sacattergo(lon=lon, lat=lat)]


my_layout = layout(title="Global earthquake")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filenname="global_earthquakes.html")
