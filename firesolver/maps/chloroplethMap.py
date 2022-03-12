from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

#Generate the heat map of risk for each tile
def generateRiskMap(saveMap, filePath):
    
    #Open and load the generated json file containing the longitudes and latitudes for each zone
    with urlopen('/Users/gregkean/Desktop/EngComp/cec/data') as response:
        zoneData = json.load(response)

    #Open and load the csv containing the generated risk values for each zones
    riskData = pd.read_csv("https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/metric_output.csv",
                    dtype={"fips": str})

    #Create the choropleth map using the data loaded above
    fig = px.choropleth_mapbox(riskData, geojson=zoneData, locations='fips', color='unemp',
                            color_continuous_scale="Viridis",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=6.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Fire Probability'},
                            title="Fire Probability Heat Map",
                            )
    fig.update_traces(marker_line_width=0)
    fig.show()