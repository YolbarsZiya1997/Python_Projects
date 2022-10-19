import csv
from datetime import datetime
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

file_name = 'data/world_fires_1_day.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)

    # Get brightness, lats, lon, and date.
    dates, brightnesses = [], []
    lons, lats = [], []
    hover_texts = []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        lon = row[1]
        lat = row[0]
        label = f"{current_date.strftime('%d%m%y')} - {brightness}"
        dates.append(current_date)
        brightnesses.append(brightness)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(label)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bri/20 for bri in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]
my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig)