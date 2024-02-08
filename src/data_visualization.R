# data_visualiation.R
#
# data_cleaning.py must be run prior to running this file, otherwise it won't work.

# Add libraries here.
install.packages(c("wordcloud2", "rjson"))

library("rjson")
library("wordcloud2")

main_table <- fromJSON(file = paste("json_data/main_table.json"))
frequency_table <- fromJSON(file = paste("json_data/frequency_table.json"))

# main_df <- data.frame(
#   ID = main_table[1],
#   Flavor_1 = main_table[2],
#   Flavor_2 = main_table[3],
#   Flavor_3 = main_table[4],
#   Flavor_4 = main_table[5],
#   Flavor_5 = main_table[6]
# )

# Word Cloud
freq_df <- data.frame(
  word = frequency_table[1],
  freq = frequency_table[2]
)

# For some reason it just puts the masking image over the word cloud.
wordcloud2(data = freq_df, size = 1, color = "random-light", backgroundColor = "gray")
