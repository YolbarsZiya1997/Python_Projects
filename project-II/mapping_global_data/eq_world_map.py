import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

file_name = 'data/eq_data_30_day_m1.json'
with open(file_name) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'YlGnBu',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig)           # You can add the filename you want to save it as after the comma

