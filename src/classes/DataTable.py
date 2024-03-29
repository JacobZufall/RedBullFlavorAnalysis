import csv
from csv import reader


class DataTable:
    def __init__(self, file: str) -> None:
        """
        A basic class that takes data from a CSV file and stores it in a row. It is then formatted to removed
        non-data text.
        :param file: The path of the CSV file to read.
        """
        self.rows: list[any] = []
        self.sdata: any = []

        csv_reader: reader = csv.reader(open(file))

        for row in csv_reader:
            self.rows.append(row)

        # This loop takes the data from the CSV file and only puts the needed data into a new table.
        for i, v in self.rows:
            if v == "What are your top 5 Red Bull flavors?":
                continue

            self.sdata.append(v.split(","))

        # This loop removes the whitespace from the data.
        for x in range(0, len(self.sdata)):
            for y in range(0, len(self.sdata[x])):
                self.sdata[x][y] = self.sdata[x][y].strip()

        # Formatted data, manipulated by different classes/instances.
        self.fdata: any = self.sdata
