from src.classes.red_bull_table import RedBullTable


class FlavorFreqTable(RedBullTable):
    def __init__(self, input_data: list[any]) -> None:
        super().__init__(input_data=input_data)

        self.sdata = self.fdata
        self.fdata = {
            "word": [],
            "freq": []
        }

        for x in self.sdata:
            for y in self.sdata[x]:
                if x == "id" or y == "None":
                    continue

                if y not in self.fdata["word"]:
                    self.fdata["word"].append(y)

                try:
                    self.fdata["freq"][self.fdata["word"].index(y)] += 1
                except IndexError:
                    self.fdata["freq"].append(1)

