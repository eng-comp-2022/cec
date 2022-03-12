
import plotly.express as px

import json
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

   
# Opening JSON file
f = open('geodata.json')
   
# returns JSON object as 
# a dictionary
json_data = json.load(f)

fig = px.choropleth_mapbox(df, geojson=json_data, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 47.7466829787486, "lon": -65.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
