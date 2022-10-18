import csv
import matplotlib.pyplot as plt
from datetime import datetime


def temp_getter(filename, date_index, high_temp_index, low_temp_index):
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_temp_index])
                low = int(row[low_temp_index])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get weather data for sitka.
file_name = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
temp_getter(file_name, date_index=2, high_temp_index=5, low_temp_index=6)

# Plot the sitka weather data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Get weather data for death valley
file_name = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
temp_getter(file_name, date_index=2, high_temp_index=4, low_temp_index=5)

# Plot the sitka weather data
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Formatting the plot
title = 'Daily high and low temperatures -2018 \n Sitka, AK and Death Vallley, CA'
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(10, 130)

plt.show()
