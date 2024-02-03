"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""

import os
import csv
from csv import reader
from typing import TextIO
from classes.red_bull_table import RedBullTable

# This should be the name of the desired CVS file with the filetype excluded.
file_name: str = "20240202"

file: TextIO = open(f"csv_data/{file_name}.csv")
csvreader: reader = csv.reader(file)

rows: list[any] = []
for row in csvreader:
    rows.append(row)

# This folder is used by data_visualization.R.
output: str = "export"
if not os.path.exists(output):
    os.makedirs(output)

main_table: RedBullTable = RedBullTable(rows)
main_table.save_json("main_table")
