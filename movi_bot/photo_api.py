import requests
import json

class Picsum:
    def __init__(self, TOKEN):
        self.token = TOKEN

    def getAccountInfo(self):
        URL = "https://api.telegra.ph/getAccountInfo?access_token={self.token}&fields=[\"short_name\",\"page_count\"]"
        response = requests.get()
        print(response)


if __name__ == '__main__':
    picsum = picsum