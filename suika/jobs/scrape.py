from typing import Final


class BeerScrape:
    API_URL: Final = 'https://www.vinbudin.is/addons/origo/module/ajaxwebservices/search.asmx/DoSearch'

    def scrape(self):
        print(self.API_URL)
