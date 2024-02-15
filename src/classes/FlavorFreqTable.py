from src.classes.RedBullTable import RedBullTable


class FlavorFreqTable(RedBullTable):
    def __init__(self, file: str) -> None:
        super().__init__(file=file)

        self.sdata: dict[str:list[str]] = self.fdata
        self.fdata: dict[str:list[str | int]] = {
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
