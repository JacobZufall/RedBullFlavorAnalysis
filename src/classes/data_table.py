import os
import json


class DataTable:
    def __init__(self, input_data: list[any]) -> None:
        """

        :param input_data:
        """
        self.sdata: any = []

        # This loop takes the data from the CVS file and only puts the needed data into a new table.
        for i, v in input_data:
            if v == "What are your top 5 Red Bull flavors?":
                continue

            self.sdata.append(v.split(","))

        # This loop removes the whitespace from the data.
        for x in range(0, len(self.sdata)):
            for y in range(0, len(self.sdata[x])):
                self.sdata[x][y] = self.sdata[x][y].strip()

        # Formatted data, manipulated by different classes/instances.
        self.fdata: any = self.sdata

    def save_json(self, file_name: str) -> None:
        """
        Saves self.fdata to a JSON file in /json_data/.
        :param file_name: The name of the file the data is being saved to.
        :return: Nothing
        """
        new_path: str = "json_data"

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        with open(f"json_data/{file_name}.json", "w") as file:
            json.dump(self.fdata, file, indent=4)
