from src.classes.data_table import DataTable


class RedBullTable(DataTable):
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

    def __init__(self,  input_data: list[any]):
        super().__init__(input_data=input_data)

        self.fdata: dict[str:list[str]] = {
            "id": [],
            "flavor_1": [],
            "flavor_2": [],
            "flavor_3": [],
            "flavor_4": [],
            "flavor_5": []
        }

        for x in range(0, len(self.sdata)):
            self.fdata["id"].append(x + 1)

            for y in range(0, 5):
                # People were requested to enter up to 5 flavors, but were permitted to do less than 5. In this case,
                # we need to fill in "None" so that we know there's a blank space.
                if not len(self.sdata[x]) < 5:
                    self.insert_data(self.sdata[x][y], y)

                else:
                    # If there's less than 5, we need to insert "None" only where they didn't put one. For example,
                    # if they only selected two flavors, this will start inserting "None" the third time this loops
                    # around. It'll go to else for the first two loops, however.
                    if len(self.sdata[x]) < y + 1:
                        self.fdata[f"flavor_{y + 1}"].append("None")
                    else:
                        self.insert_data(self.sdata[x][y], y)

    def insert_data(self, check_data: str, loop_var: int) -> None:
        """
        A very inefficient way to clean the data. Each condition specifies an observed mistake or spot where data
        needs to be manually corrected. If no mistake is present, it'll insert the data as-is.
        :param check_data: The data to be checked and corrected (if applicable).
        :param loop_var: What increment of the loop the function is called on.
        :return: Nothing.
        """
        if check_data == "AÃ§aÃ­ Berry":
            self.fdata[f"flavor_{loop_var + 1}"].append("Acai Berry")

        # Some people didn't follow instructions.
        elif check_data.lower() == "sugar free":
            self.fdata[f"flavor_{loop_var + 1}"].append("Original")

        # This one is on me for forgetting it.
        elif check_data == "Ocean Blast (Lychee)" or check_data == "Lychee":
            self.fdata[f"flavor_{loop_var + 1}"].append("Ocean Blast")

        # For lime and limeade, I added the edition in parentheses for clarification, but it needs to be removed.
        elif check_data == "Lime (Silver Edition)":
            self.fdata[f"flavor_{loop_var + 1}"].append("Lime")

        elif check_data == "Limeade (Lime Edition)":
            self.fdata[f"flavor_{loop_var + 1}"].append("Limeade")

        else:
            if check_data in self.valid_flavors:
                self.fdata[f"flavor_{loop_var + 1}"].append(check_data)
