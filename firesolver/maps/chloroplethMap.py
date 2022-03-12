from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

#Generate the heat map of risk for each tile
def generateMetricMap(saveMap, filePath):
    
    #Open and load the generated json file containing the longitudes and latitudes for each zone
    with urlopen('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/zoneData.json') as response:
        zoneData = json.load(response)

    #Open and load the csv containing the generated risk values for each zones
    riskData = pd.read_csv('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/metric_output.csv',
                    dtype={"fips": str})

    #Create the choropleth map using the data loaded above
    fig = px.choropleth_mapbox(riskData, geojson=zoneData, locations='fips', color='unemp',
                            color_continuous_scale="Sunset",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=5.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Fire Probability'},
                            title="Fire Probability Heat Map",
                            )
    
    #Remove the borders from each zone, as the entire map is black if you do not
    fig.update_traces(marker_line_width=0)
    
    # If this function was activated by the 'Generate Map' button, make it pop up in the browser
    if saveMap == False:
        fig.show()

    # If this function was activated by the 'Save Map' button, save it without making the map pop up in the browser
    if saveMap == True:
        fig.write_image(
            filePath + "/MetricHeatmap.png"
        )  # Uses kaleido (pip install -U kaleido)
        
        
        

#Generate the heat map of risk for each tile
def generateRiskMap(saveMap, filePath):
    
    
    
    #Open and load the generated json file containing the longitudes and latitudes for each zone
    with urlopen('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/zoneData.json') as response:
        zoneData = json.load(response)

    #Open and load the csv containing the generated risk values for each zones
    riskData = pd.read_csv('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/metric_output.csv',
                    dtype={"fips": str})

    #Create the choropleth map using the data loaded above
    fig = px.choropleth_mapbox(riskData, geojson=zoneData, locations='fips', color='unemp',
                            color_continuous_scale="Sunset",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=5.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Fire Probability'},
                            title="Fire Probability Heat Map",
                            )
    
    #Remove the borders from each zone, as the entire map is black if you do not
    fig.update_traces(marker_line_width=0)
    
    # If this function was activated by the 'Generate Map' button, make it pop up in the browser
    if saveMap == False:
        fig.show()

    # If this function was activated by the 'Save Map' button, save it without making the map pop up in the browser
    if saveMap == True:
        fig.write_image(
            filePath + "/MetricHeatmap.png"
        )  # Uses kaleido (pip install -U kaleido)
        
        
        
        
#Generate the choropleth map. Arguments given represent whether this is from stage one or stage two
def generateChoroplethMap(saveMap, filePath, stage):
        
    #Open and load the json file containing the longitudes and latitudes for each zone
    with urlopen('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/zoneData.json') as response:
        zoneData = json.load(response)

    #Open and load the csv containing the generated risk values for each zones
    riskData = pd.read_csv('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/metric_output.csv',
                    dtype={"fips": str})

    #Initialize the file name in case it needs to be saved
    fileExtension = ""
    
    #Initialize the figure to be edited
    fig = px.choropleth_mapbox()

    if(stage == 1):
        fileExtension = "MetricHeatmap.png"
        
        #Create the choropleth map using the data loaded above
        fig = px.choropleth_mapbox(riskData, geojson=zoneData, locations='fips', color='unemp',
                            color_continuous_scale="Sunset",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=5.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Fire Probability'},
                            title="Fire Probability Heat Map",
                            )
        
        
    else:
        fileExtension = "MetricHeatmap.png"
        
        #Create the choropleth map using the data loaded above
        fig = px.choropleth_mapbox(riskData, geojson=zoneData, locations='fips', color='unemp',
                            color_continuous_scale="Siridis",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=5.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Signifigance'},
                            title="Signifigance Heat Map",
                            )
    
        

    
    #Remove the borders from each zone, as the entire map is black if you do not
    fig.update_traces(marker_line_width=0)
    
    # If this function was activated by the 'Generate Map' button, make it pop up in the browser
    if saveMap == False:
        fig.show()

    # If this function was activated by the 'Save Map' button, save it without making the map pop up in the browser
    if saveMap == True:
        fig.write_image(filePath + fileExtension)  # Uses kaleido (pip install -U kaleido)
        