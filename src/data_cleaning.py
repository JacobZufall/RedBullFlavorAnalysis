"""
data_cleaning.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""

import os
from classes.RedBullTable import RedBullTable
from classes.FlavorFreqTable import FlavorFreqTable

# This should be the name of the desired CSV file (with the filetype excluded).
file_name: str = "20240202"
# Folders used to store data that are excluded from Git.
folders: list[str] = ["../json_data", "../export"]

for folder in folders:
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass


path: str = f"../csv_data/{file_name}.csv"

main_table: RedBullTable = RedBullTable(path)
main_table.save_json("main_table")

frequency_table: FlavorFreqTable = FlavorFreqTable(path)
frequency_table.save_json("frequency_table")
