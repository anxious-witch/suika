import click
from flask.cli import with_appcontext
from suika.jobs.scrape import BeerScrape


@click.command('scrape')
@with_appcontext
def scrape():
    scraper = BeerScrape()
    scraper.run()
