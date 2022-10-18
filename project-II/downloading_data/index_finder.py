import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename='data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    first_row = next(reader)

    # Get the indecise.
    for index, column_headers in enumerate(first_row):
        print(index, column_headers)
