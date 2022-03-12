import plotly.graph_objects as go
import pandas as pd


# ##############################

# Generate the map of NB using a csv created by the optimization
def generateMap(saveMap, filePath):

    # Fake Data to show form it should take, as well as for building/testing
    # Format is City, Lat, Lon, Type
    data = [
        {"City": "Freddy", "Lat": 45.9635895, "Lon": -66.643115, "Type": 1},
        {"City": "SJ", "Lat": 45.269598, "Lon": -66.052822, "Type": 2},
        #   {"City": "Moncton", "Lat": 46.088261, "Lon": -64.782986, "Type": 3},
        #  {"City": "Center", "Lat": 46.652598, "Lon": -66.170557, "Type": 3}
    ]

    # Set the colours for each tower type (Type 1 is purple, Type 2 is red, Type 3 is orange)
    colors = ["rgb(169, 19, 214)", "rgb(214, 19, 52)", "rgb(214, 139, 19)"]
    # Set the tower types to be used and iterated through
    types = {1: "Type 1", 2: "Type 2", 3: "Type 3"}
    # Set the radius for each tower type
    diam = {1: 88.55, 2: 88.55, 3: 110}

    # Create the base figure to be edited
    fig = go.Figure()

    # config = {"displayModeBar": False}

    # # Iterate through the data list to
    # for i in range(len(data)):
    #     tempLon = data[i]["Lon"]
    #     tempLat = data[i]["Lat"]
    #     towerType = data[i]["Type"]
    #     fig.add_trace(
    #         go.Scattergeo(
    #             # Pull all the necessary data
    #             text=data[i]["City"],
    #             name=data[i]["City"] + ", Type " + str(towerType),
    #             lat=[tempLat],
    #             lon=[tempLon],
    #             marker=dict(
    #                 sizemode="diameter",  # THIS MEANS THE BUBBLES USE DIAMETER, KEEP IN MIND DURING CALCULATION
    #                 size=diam[towerType],  # Size to scale
    #                 color=colors[towerType - 1],
    #                 line_width=0,
    #                 opacity=0.80,
    #             ),
    #         )
    #     )

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


# Generate a text file containing data on the optimized placements of the towers
def generateText(filePath):

    # Fake data
    data = [
        {"City": "Freddy", "Lat": 45.9635895, "Lon": -66.643115, "Type": 1},
        {"City": "SJ", "Lat": 45.269598, "Lon": -66.052822, "Type": 2},
        {"City": "Moncton", "Lat": 46.088261, "Lon": -64.782986, "Type": 3},
    ]

    # Open a file with the given at the given location to write to
    with open(filePath + "/fireTowerPlacement.txt", "w") as f:
        # For each datapoint, write to the file
        for i in range(len(data)):
            f.write(
                "City: "
                + data[i]["City"]
                + ", Type "
                + str(data[i]["Type"])
                + "\n\t"
                + "Latitude: "
                + str(data[i]["Lat"])
                + "\n\t"
                + "Longitude: "
                + str(data[i]["Lon"])
                + "\n"
            )
