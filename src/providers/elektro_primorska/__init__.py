
from src.infrastructure.scraper import Scraper
from src.providers.elektro_primorska.parser import Parser

class ElektroPrimorska(Scraper):
    def __init__(self) -> None:
        super().__init__("https://elektro-primorska.si/wp-admin/admin-ajax.php")

    def handle(self):
        raw_data = self.raw_data()
        parser = Parser(self.filters)
        parsed_data = parser.parse(raw_data)

        return parsed_data
