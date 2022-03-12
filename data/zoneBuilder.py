# #The data given to us was in the form of a perfect rectangle. Our map software uses longitudes and latitudes and allows for much more nuances areas.
# #In this file, we will build up the areas using simple math on the longitudes and latitudes of a simplified (rectangular) NB.

# #Here is an example of a line definining a box
# #{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {"GEO_ID": "0500000US01001", "STATE": "01", "COUNTY": "001", "NAME": "Autauga", "LSAD": "County", "CENSUSAREA": 594.436}, "geometry": {"type": "Polygon", "coordinates": [[[-86.496774, 32.344437], [-86.717897, 32.402814], [-86.814912, 32.340803], [-86.890581, 32.502974], [-86.917595, 32.664169], [-86.71339, 32.661732], [-86.714219, 32.705694], [-86.413116, 32.707386], [-86.411172, 32.409937], [-86.496774, 32.344437]]]}, "id": "01001"},

import csv


# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

    # csv data
rows = [
        {'name': 'Albania',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALB'},
        {'name': 'Algeria',
        'area': 2381741,
        'country_code2': 'DZ',
        'country_code3': 'DZA'},
        {'name': 'American Samoa',
        'area': 199,
        'country_code2': 'AS',
        'country_code3': 'ASM'}
    ]


with open('/Users/gregkean/Desktop/zones.csv','w') as file:
    for i in range(0, 3):
        toWrite = "{\"type\": \"FeatureCollection\", \"features\": [{\"type\": \"Feature\", \"properties\": {\"AREA\": 1}, \"geometry\": {\"type\": \"Polygon\", \"coordinates\": [[[-86.496774, 32.344437], [-86.717897, 32.402814], [-86.814912, 32.340803], [-86.890581, 32.502974], [-86.917595, 32.664169], [-86.71339, 32.661732], [-86.714219, 32.705694], [-86.413116, 32.707386], [-86.411172, 32.409937], [-86.496774, 32.344437]]]}, \"id\": \"" + str(i) + "\"},"

        file.write(toWrite)
        file.write('\n')

# with open('/Users/gregkean/Desktop/zones.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(0, 3):
#             toWrite = '{\"type\": \"FeatureCollection\", \"features\": [{\"type\": \"Feature\", \"properties\": {\"AREA\": 1}, \"geometry\": {\"type\": \"Polygon\", \"coordinates\": [[[-86.496774, 32.344437], [-86.717897, 32.402814], [-86.814912, 32.340803], [-86.890581, 32.502974], [-86.917595, 32.664169], [-86.71339, 32.661732], [-86.714219, 32.705694], [-86.413116, 32.707386], [-86.411172, 32.409937], [-86.496774, 32.344437]]]}, \"id\": \"" + str(i) + "\"'
#             writer.writerow([toWrite])
    

# def generateZones(filePath):
    
#     # csv header
#     fieldnames = ['name', 'area', 'country_code2', 'country_code3']

#     # csv data
#     rows = [
#         {'name': 'Albania',
#         'area': 28748,
#         'country_code2': 'AL',
#         'country_code3': 'ALB'},
#         {'name': 'Algeria',
#         'area': 2381741,
#         'country_code2': 'DZ',
#         'country_code3': 'DZA'},
#         {'name': 'American Samoa',
#         'area': 199,
#         'country_code2': 'AS',
#         'country_code3': 'ASM'}
#     ]

#     idCounter = 0

#     with open('/Users/gregkean/Desktop/zones.csv', 'w', encoding='UTF8', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow("{\"type\": \"FeatureCollection\", \"features\": [{\"type\": \"Feature\", \"properties\": {\"GEO_ID\": \"0500000US01001\", \"STATE\": \"01\", \"COUNTY\": \"001\", \"NAME\": \"Autauga\", \"LSAD\": \"County\", \"CENSUSAREA\": 594.436}, \"geometry\": {\"type\": \"Polygon\", \"coordinates\": [[[-86.496774, 32.344437], [-86.717897, 32.402814], [-86.814912, 32.340803], [-86.890581, 32.502974], [-86.917595, 32.664169], [-86.71339, 32.661732], [-86.714219, 32.705694], [-86.413116, 32.707386], [-86.411172, 32.409937], [-86.496774, 32.344437]]]}, \"id\": \"01001\"},")
    



# # Generate a text file containing data on the optimized placements of the towers
# def generateText(filePath):

#     # Fake data
#     data = [
#         {"City": "Freddy", "Lat": 45.9635895, "Lon": -66.643115, "Type": 1},
#         {"City": "SJ", "Lat": 45.269598, "Lon": -66.052822, "Type": 2},
#         {"City": "Moncton", "Lat": 46.088261, "Lon": -64.782986, "Type": 3},
#     ]

#     # Open a file with the given at the given location to write to
#     with open(filePath + "/fireTowerPlacement.txt", "w") as f:
#         # For each datapoint, write to the file
#         for i in range(len(data)):
#             f.write(
#                 "City: "
#                 + data[i]["City"]
#                 + ", Type "
#                 + str(data[i]["Type"])
#                 + "\n\t"
#                 + "Latitude: "
#                 + str(data[i]["Lat"])
#                 + "\n\t"
#                 + "Longitude: "
#                 + str(data[i]["Lon"])
#                 + "\n"
#             )
