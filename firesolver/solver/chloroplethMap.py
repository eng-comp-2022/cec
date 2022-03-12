from urllib.request import urlopen
import json

def generateMap(saveMap, filePath):
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                    dtype={"fips": str})

    import plotly.express as px

    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                            color_continuous_scale="Viridis",
                            range_color=(0, 12),
                            mapbox_style="carto-positron",
                            zoom=6.5, center = {"lon":-66.170557, "lat":46.652598},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()