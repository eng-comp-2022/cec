import plotly.graph_objects as go
import pandas as pd
from solver import fire_resource_plan

# Generate the map of NB using a csv created by the optimization
def generateStationMap(saveMap, filePath, location):
    
    #Initialize top left lat and lon of NB and epsilons needed to convert grid coordinates to lats and longs
    top_left_lon = -67.779559
    top_left_lat = 47.846172
    epsLat = 0.009
    epsLon = 0.0132

    # Set the colours for each tower type (Type A is yellow, Type B is red, Type C is black)
    colors = ["rgb(255, 255, 0)", "rgb(255, 0, 0)", "rgb(0, 0, 0)"]
    # Set the tower types to be used and iterated through
    types = {1: "Type A: Water Plane", 2: "Type B: Fire Truck", 3: "Type C: ATV"}
    # Set the radius for each tower type
    diam = [200, 120, 80]

    # Create the base figure to be edited
    fig = go.Figure()

    #Disable the display bar
    config = {"displayModeBar": False}
    
    #Initialize the data
    data = {}
    
    #Check which location is attempting to be viewed
    if(location == "Saint John"):
        loc = 2
    if(location == "Moncton"):
        loc = 3
    if(location == "Fredericton"):
        loc = 4
    if(location == "Miramichi"):
        loc = 5
    if(location == "Bathurst"):
        loc = 6
    if(location == "Mactaquac"):
        loc = 7
    if(location == "Mount Carleton"):
        loc = 8
    if(location == "Parlee Beach"):
        loc = 9
    if(location == "Kouchibouguac"):
        loc = 10
    if(location == "Fundy"):
        loc = 11
    if(location == "Gagetown"):
        loc = 12
        
    #Get the data for the given location
    data = fire_resource_plan.assign_firestation_to_key_locs()
    data = data[loc]
    
    # Iterate through the data list to draw the bubbles
    for i in range(len(data)):
        #These have to be grabbed outside the trace
        tempLon = top_left_lon + (data[i][1] * epsLon)
        tempLat = top_left_lat - (data[i][0] * epsLat)
        towerType = data[i][2]
        #Convert types to ints so they can grab from their respective lists
        if towerType == 'A':
            towerInt = 0
        if towerType == 'B':
            towerInt = 1
        if towerType == 'C':
            towerInt = 2
        fig.add_trace(
            go.Scattergeo(
                # Give all necessary data
                text= "Type " + str(towerType),
                name= "Type " + str(towerType),
                lat=[tempLat],
                lon=[tempLon],
                marker=dict(
                    sizemode="diameter",  # THIS MEANS THE BUBBLES USE DIAMETER, KEEP IN MIND DURING CALCULATION
                    size=diam[towerInt],  # Size to scale
                    color=colors[towerInt],
                    line_width=0,
                    opacity=0.5,
                ),
            )
        )

    # Set the layout of the map now that we have data generated
    fig.update_layout(
        # Title the map
        title=go.layout.Title(text="Optimized Firetower Placement"),
        showlegend=True,
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
            filePath + "/fireStationMap.png"
        )  # Uses kaleido (pip install -U kaleido)
