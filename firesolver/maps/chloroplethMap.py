from urllib.request import urlopen
import json
import pandas as pd

def generateRiskMap(saveMap, filePath):
    with urlopen('https://raw.githubusercontent.com/eng-comp-2022/cec/main/data/zoneData.json') as response:
        zones = json.load(response)

    
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                    dtype={"fips": str})

    import plotly.express as px

    fig = px.choropleth_mapbox(df, geojson=zones, locations='fips', color='unemp',
                            color_continuous_scale="Viridis",
                            range_color=(0, 1),
                            mapbox_style="carto-positron",
                            zoom=6.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'Fire Probability'}
                            )
   
    fig.show()