"""
data_visualization.py

This file turns the CSV file into a table and saves it to a JSON file to make the data easier to use.
"""
from typing import Any
import os
import numpy as np
from numpy import ndarray, dtype
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
from classes.RedBullTable import RedBullTable

# This should be the name of the desired CSV file (with the filetype excluded).
file_name: str = "20240202"
path: str = f"../csv_data/{file_name}.csv"

main_table: RedBullTable = RedBullTable(path)

# WORDCLOUD

# A list which contains every flavor by itself, not grouped.
all_data: list[str] = []

for i, v in main_table.fdata.items():
    if i != "id":
        for j in v:
            if j != "None":
                all_data.append(j)

color_map: dict[str:str] = {
    "Original": "#284280",
    "Acai Berry": "#6A2171",
    "Arctic-Berry": "#D3EAF4",
    "Beach Breeze": "#029AB6",
    "Blueberry": "#262F74",
    "Cactus Fruit": "#209B45",
    "Cranberry": "#9E1816",
    "Coconut Berry": "white",
    "Dragon Fruit": "#209B45",
    "Fig Apple": "#135A57",
    "Grapefruit Twist": "#E22D55",
    "Juneberry": "#006CB5",
    "Kiwi-Apple": "#88BA21",
    "Lime": "gray",
    "Limeade": "#007831",
    "Tangerine": "#E7651D",
    "Ocean Blast": "#01BEDB",
    "Peach-Nectarine": "#67171A",
    "Pear": "#2B6350",
    "Pear Cinnamon": "#B71A44",
    "Plum Twist": "#570C27",
    "Pomegranate": "#8C1E31",
    "Strawberry Apricot": "#F18A25",
    "Tropical": "#E2AF18",
    "Watermelon": "#C5392F",
}


def get_color(word: str, font_size, position, orientation, random_state, **kwargs) -> str:
    return color_map.get(word, "white")


mask: ndarray[Any, dtype[Any]] = np.array(Image.open("../resources/masking/bull.png"))

wc: any = WordCloud(width=3_000, height=3_000, collocations=False, regexp=r"\w[\w' -]+", color_func=get_color,
                    mask=mask).generate("+".join(all_data))

plt.figure(figsize=(30, 30))
plt.imshow(wc)
plt.axis("off")

try:
    plt.savefig("../exports/wordcloud.png")
except FileNotFoundError:
    os.mkdir("../exports")
    plt.savefig("../exports/wordcloud.png")
