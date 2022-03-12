
import plotly.express as px
import json
import pandas as pd
df = pd.read_csv("/Users/gregkean/Desktop/EngComp/cec/data/metric_output.csv",
                   dtype={"fips": str})

   
# Opening JSON file
f = open("/Users/gregkean/Desktop/EngComp/cec/data/zoneData.json")
   
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
fig.update_traces(marker_line_width=0)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()