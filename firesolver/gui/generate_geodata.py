import json

top_left_lat = -67.66776684614666
top_left_lon = 47.74668297874867
eps = 0.01125514978108399
eps2 = 0.007
width = 246
height = 304

json_data = {"type": "FeatureCollection", "features": []}
id = 0

lat = top_left_lat
lon = top_left_lon
for i in range(width):
    for j in range(height):
        json_data["features"].append({"type": "Feature", "properties": {"AREA": 1}, "geometry": {"type": "Polygon", "coordinates": [[[lat, lon], [lat, lon-eps], [lat+eps, lon-eps], [lat+eps, lon]]]}, "id": str(id)})
        id += 1
        lon -= eps2
    lat += eps
    lon = top_left_lon

with open('geodata.json', 'w') as f:
    json.dump(json_data, f)