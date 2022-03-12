import plotly.graph_objects as go
import pandas as pd


# ##############################

# Generate the map of NB using a csv created by the optimization
def generateStationMap(saveMap, filePath, location):
    
    

    # Fake Data to show form it should take, as well as for building/testing
    # Format is City, Lat, Lon, Type
    data = [
        {"City": "Saint John", "Lat": 45.269598, "Lon": -66.052822, "Type": 3},
        {"City": "Moncton", "Lat": 46.088879, "Lon": -64.775818, "Type": 3},
        {"City": "Fredericton", "Lat": 45.959221, "Lon": -66.640350, "Type": 3},
        {"City": "Miramichi", "Lat": 47.027908, "Lon": -65.469482, "Type": 2},
        {"City": "Bathurst", "Lat": 47.61922, "Lon": -65.66046, "Type": 2},
        {"City": "Mactaquac", "Lat": 45.95429, "Lon": -66.88959, "Type": 1},
        {"City": "Mount Carelton", "Lat": 47.40786, "Lon": -66.91740, "Type": 1},
        {"City": "Parlee Beach", "Lat": 46.23998, "Lon": -64.51020, "Type": 2},
        {"City": "Kouchibouguac", "Lat": 46.79534, "Lon": -65.05671, "Type": 2},
        {"City": "Fundy", "Lat": 45.61394, "Lon": -65.03284, "Type": 3},
        {"City": "Gagetown", "Lat": 45.78214, "Lon": -66.14849, "Type": 2}
    ]
    
    #Initialize station location, and epsilons needed to convert grid coordinates to lats and longs
    stationData = {}
    top_left_lon = -67.779559
    top_left_lat = 47.846172
    epsLat = 0.009
    epsLon = 0.0132

    # Set the colours for each tower type (Type A is yellow, Type B is red, Type C is black)
    colors = ["rgb(255, 255, 0)", "rgb(255, 0, 0)", "rgb(0, 0, 0)"]
    # Set the tower types to be used and iterated through
    types = {1: "Type A: Water Plane", 2: "Type B: Fire Truck", 3: "Type C: ATV"}
    # Set the radius for each tower type
    diam = {1: 200, 2: 120, 3: 80}

    # Create the base figure to be edited
    fig = go.Figure()

    #Disable the display bar
    config = {"displayModeBar": False}
    
    #Initialize the data
    data = {}
    
    #Check which location is attempting to be viewed
    if(location == "Saint John"):
        loc = 0
    if(location == "Moncton"):
        loc = 1
    if(location == "Fredericton"):
        loc = 2
    if(location == "Miramichi"):
        loc = 3
    if(location == "Bathurst"):
        loc = 4
    if(location == "Mactaquac"):
        loc = 5
    if(location == "Mount Carleton"):
        loc = 6
    if(location == "Parlee Beach"):
        loc = 7
    if(location == "Kouchibouguac"):
        loc = 8
    if(location == "Fundy"):
        loc = 9
    if(location == "Gagetown"):
        loc = 10
    
    # Iterate through the data list to
    for i in range(len(data)):
        tempLon = data[i]["Lon"]
        tempLat = data[i]["Lat"]
        towerType = data[i]["Type"]
        fig.add_trace(
            go.Scattergeo(
                # Pull all the necessary data
                text=data[i]["City"],
                name=data[i]["City"] + ", Type " + str(towerType),
                lat=[tempLat],
                lon=[tempLon],
                marker=dict(
                    sizemode="diameter",  # THIS MEANS THE BUBBLES USE DIAMETER, KEEP IN MIND DURING CALCULATION
                    size=diam[towerType],  # Size to scale
                    color=colors[towerType - 1],
                    line_width=0,
                    opacity=0.5,
                ),
            )
        )

    # Set the layout of the map now that we have data generated
    fig.update_layout(
        # Title the map
        title=go.layout.Title(text="Optimized Firetower Placement"),
        # Give the layout (zoom, etc) of the map
        geo=go.layout.Geo(
            resolution=50,  # 1:50 resolution
            scope="north america",  # Render only north america (that it is the closest to only NB possible)
            showframe=True,  # Show the frame to deliniate between map and non-map
            showcoastlines=True,  # Highlight the coastlines as NB is on the coast
            landcolor="rgb(208, 240, 192)",  # Set the land colour to be 'tea'
            countrycolor="black",  # Colour of country outlines
            coastlinecolor="black",  # Colour of coastal outline
            showlakes=True,
            lakecolor="Blue",  # Show lakes to get a better view of NB
            showrivers=True,
            rivercolor="Blue",  # Show rivers as SJ river is a big fixture of NB
            showocean=True,
            oceancolor="LightBlue",  # Shows ocean as NB is on the coast
            center=dict(
                lon=-66.170557, lat=46.652598
            ),  # Center the view on the center of NB
            lonaxis_range=[
                -75,
                -57,
            ],  # Set the default range of the longitude to be zoomed to NB, this is ~1386km
            lataxis_range=[
                45,
                47,
            ],  # Set the default range of the latitude to be zoomed to NB, this is ~222km
            domain=dict(x=[0, 1], y=[0, 1]),  # Set the domain
        ),
        dragmode=False,  # Disable scrolling and zooming to keep the sizes accurate
    )

    # If this function was activated by the 'Generate Map' button, make it pop up in the browser
    if saveMap == False:
        fig.show(config=config)

    # If this function was activated by the 'Save Map' button, save it without making the map pop up in the browser
    if saveMap == True:
        fig.write_image(
            filePath + "/fireTowerMap.png"
        )  # Uses kaleido (pip install -U kaleido)
