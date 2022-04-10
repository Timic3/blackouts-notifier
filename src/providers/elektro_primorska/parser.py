from bs4 import BeautifulSoup

class Parser:
    def __init__(self, filters={}) -> None:
        self.filters = filters

    def filter(self, row):
        for (key, value) in self.filters.items():
            if row[key] != value:
                return False
        return True

    def parse(self, text):
        data = []
        soup = BeautifulSoup(text, "html.parser")
        rows = soup.find_all("tr")

        for row in rows:
            data.append({
                "town": row["data-kraj"],
                "street": row["data-ulica-naziv"],
                "numbers": row["data-ulica-stevilke"],
                "time_start": row["data-start-datetime"],
                "time_end": row["data-end-datetime"],
                "type": row["data-tip-naziv"]
            })

        return list(filter(self.filter, data))
