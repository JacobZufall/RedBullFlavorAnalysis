# data_visualiation.R
#
# data_cleaning.py must be run prior to running this file, otherwise it won't work.

# Add libraries here.
install.packages(c("wordcloud2", "rjson"))


library("rjson")
library("wordcloud2")

json_data <- fromJSON(file = paste("json_data/main_table.json"))

main_df <- data.frame(
  ID = json_data[1],
  Flavor_1 = json_data[2],
  Flavor_2 = json_data[3],
  Flavor_3 = json_data[4],
  Flavor_4 = json_data[5],
  Flavor_5 = json_data[6]
)

# Word Cloud
