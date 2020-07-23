import json
import requests
from datetime import datetime
from suika.models.product import Product
from suika.models.price import Price


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
        data = self.__get_data(res)

        for d in data:
            product = Product(
                name=d['ProductName'],
                sku=str(d['ProductID']),
                volume=d['ProductBottledVolume'],
                abv=d['ProductAlchoholVolume'],
                country_of_origin=d['ProductCountryOfOrigin'],
                available=d['ProductIsAvailableInStores'],
                container_type=d['ProductContainerType'],
                style=d['ProductTasteGroup'],
                sub_style=d['ProductTasteGroup2'],
                producer=d['ProductProducer'],
                short_description=d['ProductShortDescription'],
                date_on_market=datetime.fromisoformat(
                    d['ProductDateOnMarket']
                ),
                season=d['ProductSeasonCode'],
            )
            sentinel = Product.query.filter_by(sku=str(d['ProductID'])).first()
            if sentinel is None:
                product.add()
            else:
                product = sentinel

            product.prices.append(
                Price(
                    price=int(d['ProductPrice']),
                    date=datetime.now()
                )
            )
            product.add()

    def __get_total(self, res) -> int:
        return json.loads(res.json()['d'])['total']

    def __get_data(self, res) -> dict:
        return json.loads(res.json()['d'])['data']
