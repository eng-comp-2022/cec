#The data given to us was in the form of a perfect rectangle. Our map software uses longitudes and latitudes and allows for much more nuanced areas.
#In this file, we will build up the areas using simple math on the longitudes and latitudes of a simplified (rectangular) NB.
#It must be run only once, and then the data will be placed in the github so that the chloropleth map can read it

# #Here is an example of a line definining a box
# {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"AREA": 1}, "geometry": {"type": "Polygon", "coordinates": [[[-67.66776684614666, 47.74668297874867], [-67.66776684614666, 47.73869097874867], [-67.65977484614666, 47.73869097874867], [-67.65977484614666, 47.74668297874867]]]}, "id": "0"}, {"type": "Feature", "properties": {"AREA": 1}, "geometry": {"type": "Polygon", "coordinates": [[[-67.66776684614666, 47.73869097874867], [-67.66776684614666, 47.73069897874867], [-67.65977484614666, 47.73069897874867], [-67.65977484614666, 47.73869097874867]]]}, "id": "1"},

import json

top_left_lon = 47.74668297874867
top_left_lat = -67.66776684614666
eps = 0.01125514978108399
eps2 = 0.0079
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
            lat -= eps2
        lon += eps
        lat = top_left_lat
        
with open("zoneData.json", "w") as f:
        json.dump(json_data, f)
