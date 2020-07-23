from suika.jobs.scrape import BeerScrape

scraper = BeerScrape()
data = scraper.scrape()

for d in data:
    print(d)
    print()
