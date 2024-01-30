"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""

import csv
import json
from _csv import reader
from typing import TextIO

file_name: str = "20240130"

file: TextIO = open(f"csv_data/{file_name}.csv")
csvreader: reader = csv.reader(file)

rows: list[any] = []
data: list[list[str]] = []

for row in csvreader:
    rows.append(row)

for i, v in rows:
    # We don't need this included in the data.
    if v == "What are your top 5 Red Bull flavors?":
        continue

    data.append(v.split(","))

# This set of nested loops trims any whitespace off of both ends of the data.
for x in range(0, len(data)):
    for y in range(0, len(data[x])):
        data[x][y] = data[x][y].strip()

with open(f"json_data/{file_name}.json", "w") as f:
    json.dump(data, f, indent=4)
