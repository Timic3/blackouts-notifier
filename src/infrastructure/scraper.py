import requests

class Scraper:
    def __init__(self, url) -> None:
        self.url = url
        self.filters = {}
        self.headers = {
            "origin": "https://elektro-primorska.si",
            "referer": "https://elektro-primorska.si/izklopi/",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        self.data = {
            "action": "get_ajax_posts",
            "map_area": "vsi",
            "map_post": "vsi",
            "map_type": "vsi"
        }

    def set_filters(self, filters):
        self.filters = filters

    def raw_data(self):
        return requests.post(self.url, headers=self.headers, data=self.data).text

    def handle(self):
        pass
