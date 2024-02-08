"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""

import os
import csv
from csv import reader
from typing import TextIO
from classes.red_bull_table import RedBullTable
from classes.flavor_freq_table import FlavorFreqTable

# This should be the name of the desired CSV file (with the filetype excluded).
file_name: str = "20240202"

file: TextIO = open(f"csv_data/{file_name}.csv")
csvreader: reader = csv.reader(file)
# Folders used to store data that are excluded from Git.
folders: list[str] = ["json_data", "export"]


for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

main_table: RedBullTable = RedBullTable(csvreader)
main_table.save_json("main_table")

frequency_table: FlavorFreqTable = FlavorFreqTable(csvreader)
frequency_table.save_json("frequency_table")
