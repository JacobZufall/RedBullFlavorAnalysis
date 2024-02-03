"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""

import csv
import os
from csv import reader
import json
from typing import TextIO

# This should be the name of the desired CVS file with the filetype excluded.
file_name: str = "20240131"

file: TextIO = open(f"csv_data/{file_name}.csv")
csvreader: reader = csv.reader(file)

rows: list[any] = []

valid_flavors: list[str] = [
    "Original",
    "Acai Berry",
    "Arctic-Berry",
    "Beach Breeze",
    "Blueberry",
    "Cactus Fruit",
    "Cranberry",
    "Coconut Berry",
    "Dragon Fruit",
    "Fig Apple",
    "Grapefruit Twist",
    "Juneberry",
    "Kiwi-Apple",
    "Lime",
    "Limeade",
    "Ocean Blast",
    "Tangerine",
    "Peach-Nectarine",
    "Pear",
    "Pear Cinnamon",
    "Plum Twist",
    "Pomegranate",
    "Strawberry Apricot",
    "Tropical",
    "Watermelon"
]

for row in csvreader:
    rows.append(row)

# I should consider condensing these tables.
data: list[list[str]] = []
json_data: dict[str:list[str]] = {
    "id": [],
    "flavor_1": [],
    "flavor_2": [],
    "flavor_3": [],
    "flavor_4": [],
    "flavor_5": []
}

for i, v in rows:
    # We don't need this included in the data.
    if v == "What are your top 5 Red Bull flavors?":
        continue

    data.append(v.split(","))

# This trims the whitespace off of the data.
for x in range(0, len(data)):
    for y in range(0, len(data[x])):
        data[x][y] = data[x][y].strip()


def insert_data(input_data: str):
    """
    A very inefficient way to clean the data. Each condition specifies an observed mistake or spot where data needs
    to be manually corrected. If no mistake is present, it'll insert the data as-is.
    :param input_data: The data to be checked and corrected (if applicable).
    :return: Nothing.
    """
    if input_data == "AÃ§aÃ­ Berry":
        json_data[f"flavor_{y + 1}"].append("Acai Berry")

    # Some people didn't follow instructions.
    elif input_data.lower() == "sugar free":
        json_data[f"flavor_{y + 1}"].append("Original")

    # This one is on me for forgetting it.
    elif input_data == "Ocean Blast (Lychee)" or input_data == "Lychee":
        json_data[f"flavor_{y + 1}"].append("Ocean Blast")

    # For lime and limeade, I added the edition in parentheses for clarification, but it needs to be removed.
    elif input_data == "Lime (Silver Edition)":
        json_data[f"flavor_{y + 1}"].append("Lime")

    elif input_data == "Limeade (Lime Edition)":
        json_data[f"flavor_{y + 1}"].append("Limeade")

    else:
        if input_data in valid_flavors:
            json_data[f"flavor_{y + 1}"].append(input_data)


for x in range(0, len(data)):

    json_data["id"].append(x + 1)

    for y in range(0, 5):
        # People were requested to enter up to 5 flavors, but were permitted to do less than 5. In this case,
        # we need to fill in "None" so that we know there's a blank space.
        if not len(data[x]) < 5:
            insert_data(data[x][y])

        else:
            # If there's less than 5, we need to insert "None" only where they didn't put one. For example,
            # if they only selected two flavors, this will start inserting "None" the third time this loops around.
            # It'll go to else for the first two loops, however.
            if len(data[x]) < y + 1:
                json_data[f"flavor_{y + 1}"].append("None")
            else:
                insert_data(data[x][y])

# Exports to JSON to be used in data_visualization.R.
new_path: str = "json_data"
output: str = "export"

if not os.path.exists(new_path):
    os.makedirs(new_path)

# This folder is used by data_visualization.R.
if not os.path.exists(output):
    os.makedirs(output)

with open(f"json_data/{file_name}.json", "w") as f:
    json.dump(json_data, f, indent=4)
