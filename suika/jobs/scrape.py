import requests
import json


class BeerScrape:
    API_URL = 'https://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/DoSearch'
    HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def scrape(self) -> dict:
        params = {
            'category': 'beer',
            'count': '0',
            'skip': '0'
        }
        res = requests.get(self.API_URL, params=params, headers=self.HEADERS)
        params['count'] = self.__get_total(res)

        res = requests.get(self.API_URL, params=params, headers=self.HEADERS)
        return self.__get_data(res)

    def __get_total(self, res) -> int:
        return json.loads(res.json()['d'])['total']

    def __get_data(self, res) -> dict:
        return json.loads(res.json()['d'])['data']
