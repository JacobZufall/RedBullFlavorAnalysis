install.packages("rjson")
library("rjson")

fileName <- "20240130"

data <- fromJSON(file=paste0("json_data/", fileName, ".json"))

print(data)