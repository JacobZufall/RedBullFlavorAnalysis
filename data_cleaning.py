"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.

The end result is one table, where each index is a table of the 5 flavors a person picked. For example:
{
    "0": {
        "0": "Cranberry",
        "1": "Coconut Berry",
        "2": "Juneberry",
        "3": "Pear",
        "4": "Pomegranate"
    },
    "1": {
        "0": "Original",
        "1": "Blueberry",
        "2": "Kiwi-Apple",
        "3": "Tangerine",
        "4": "Strawberry Apricot"
    },
}
Doing this allows me to analyze the groupings and do additional data analysis on the sample.
"""

import csv
from csv import reader
import json
from typing import TextIO
from valid_flavors import valid_flavors

# This should be the name of the desired CVS file with the filetype excluded.
file_name: str = "20240131"

file: TextIO = open(f"csv_data/{file_name}.csv")
csvreader: reader = csv.reader(file)

rows: list[any] = []
data: list[list[str]] = []
data_dict: dict[int:[dict[int:str]]] = {}

for row in csvreader:
    rows.append(row)

for i, v in rows:
    # We don't need this included in the data.
    if v == "What are your top 5 Red Bull flavors?":
        continue

    data.append(v.split(","))

# This set of nested loops trims any whitespace off of both ends of the data.
# TODO: Currently, "açaí" shows up as
#  "aÃ§aÃ­" in the resulting JSON file. Consider adding in a conditional to change the two accented characters to
#  non-accented characters.
for x in range(0, len(data)):
    for y in range(0, len(data[x])):
        data[x][y] = data[x][y].strip()

# I included an "Other" field in the survey in the event that I missed any flavors (which I did). However,
# some people cannot read, because I explicitly said if you like a sugar-free version, just select the regular
# variant. Yet, people still put "sugar-free" down. There's also the case where people aren't consistent with each
# other, and that needs to be corrected to make the visuals work better in data_visualization.R.
for x in range(0, len(data)):
    dict_row: dict[int:str] = {}

    for y in range(0, len(data[x])):
        if data[x][y] in valid_flavors:
            dict_row[y] = data[x][y]
        else:
            if data[x][y].lower() == "sugar free":
                dict_row[y] = "Original"

            if data[x][y].lower() == "lychee" or data[x][y].lower() == "ocean blast (lychee)":
                dict_row[y] = "Ocean Blast"

            # For lime and limeade, I put the edition in parentheses to clarify. However, I want this removed for visual
            # purposes.
            if data[x][y].lower() == "lime (silver edition)":
                dict_row[y] = "Lime"

            if data[x][y].lower() == "limeade (lime edition)":
                dict_row[y] = "Limeade"

            # For some reason this condition is never met.
            if data[x][y] == "A\u00a7a\u00ad Berry":
                dict_row[y] = "Açaí Berry"

    data_dict[x] = dict_row

# Exports to JSON to be used in data_visualization.R.
with open(f"json_data/{file_name}.json", "w") as f:
    json.dump(data_dict, f, indent=4)
