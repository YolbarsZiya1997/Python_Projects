import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename= 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    first_row = next(reader)

    # Get the data out.
    dates, rain_fall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall_amount = float(row[3])
        dates.append(current_date)
        rain_fall.append(rainfall_amount)

# Plot the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rain_fall, c='green', alpha=0.5)

# Formatting the plot.
plt.title('Rain Fall Amount in the Sitka Rain Forest', fontsize=26)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Amount (L)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

