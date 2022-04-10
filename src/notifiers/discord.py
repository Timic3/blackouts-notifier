import requests

class Discord:
    def __init__(self, url) -> None:
        self.url = url
    
    def handle(self, data):
        request = requests.post(self.url, json=data)
        if request.status_code not in [200, 204]:
            print("Error while sending request (%s, %s)" % (request.status_code, request.reason))
            print(request.text)
