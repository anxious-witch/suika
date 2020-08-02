import re
import json
import requests
from urllib import parse
from bs4 import BeautifulSoup
from suika.models.product import Product
from suika.models.price import Price


class BeerScrape:
    BEER_URL = 'https://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/DoSearch'
    STYLE_URL = 'https://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/GetAllBeerTaste2Categories'
    INDEX_URL = 'https://www.vinbudin.is/heim/vorur'
    HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    def run(self) -> None:
        styles = self.__get_styles()
        sub_styles = self.__get_sub_styles(styles)

        self.__get_beer(styles=styles, sub_styles=sub_styles)

    def __get_styles(self) -> dict:
        """Parse the product category page

        Internal product group codes are converted to the human-readable form
        e.g. 61IP -> IPA

        """

        res = requests.get(self.INDEX_URL)
        style_map = {}

        soup = BeautifulSoup(res.text, features='html.parser')
        product_links = soup.find_all('div', class_='voru-link')

        for link in product_links:
            beer_link = link.find(
                'a',
                href=re.compile(r'(category=beer&taste=\w+)|(taste=\w+&category=beer)')
            )

            if beer_link:
                beer_style = parse.parse_qs(
                    parse.urlsplit(beer_link['href']).query
                )['taste'][0]
                name = beer_link.find('div', class_='title').text

                style_map[beer_style] = name

        return style_map

    def __get_sub_styles(self, styles: dict) -> dict:
        """Bombard the category API to get sub-styles for the product groups

        Internal sub-style IDs are converted to a human readable form
        e.g. SESSION -> Session IPA

        """

        sub_style_map = {}

        for key in styles.keys():
            params = {
                'supertaste': key
            }

            res = requests.get(self.STYLE_URL, params=params, headers=self.HEADERS)
            data = json.loads(res.json()['d'])

            for d in data:
                sub_style_map[d['id']] = d['Description']

        return sub_style_map

    def __get_beer(self, styles=dict(), sub_styles=dict()) -> dict:
        """Get the beer catalogue from vinbudin.is

        """

        params = {
            'category': 'beer',
            'count': '0',
            'skip': '0'
        }
        res = requests.get(self.BEER_URL, params=params, headers=self.HEADERS)
        params['count'] = self.__get_total(res)

        res = requests.get(self.BEER_URL, params=params, headers=self.HEADERS)
        data = self.__get_data(res)

        for d in data:
            style_name = styles.get(d['ProductTasteGroup'], d['ProductTasteGroup'])
            sub_style_name = sub_styles.get(d['ProductTasteGroup2'], d['ProductTasteGroup2'])

            product = Product(
                name=d['ProductName'],
                sku=str(d['ProductID']),
                volume=d['ProductBottledVolume'],
                abv=d['ProductAlchoholVolume'],
                country_of_origin=d['ProductCountryOfOrigin'],
                available=d['ProductIsAvailableInStores'],
                container_type=d['ProductContainerType'],
                style=style_name,
                sub_style=sub_style_name,
                producer=d['ProductProducer'],
                short_description=d['ProductShortDescription'],
                season=d['ProductSeasonCode']
            )

            sentinel = Product.query.filter_by(sku=str(d['ProductID'])).first()
            if sentinel is None:
                product.add()
            else:
                product = sentinel

            product.prices.append(
                Price(price=int(d['ProductPrice']))
            )

            product.add()

    def __get_total(self, res) -> int:
        return json.loads(res.json()['d'])['total']

    def __get_data(self, res) -> dict:
        return json.loads(res.json()['d'])['data']
