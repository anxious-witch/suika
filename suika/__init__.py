import os
from flask import Flask
from dotenv import load_dotenv
from suika.jobs.scrape import BeerScrape
from suika.routes import index
from suika.routes import product
from suika.models.db import db, migrate


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SUIKA_DB')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.register_blueprint(index.blueprint)
    app.register_blueprint(product.blueprint)

    db.init_app(app)
    migrate.init_app(app, db)

    return app


def scheduled_scraper():
    scraper = BeerScrape()
    scraper.scrape()
