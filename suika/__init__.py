import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from suika.jobs.scrape import BeerScrape
from suika.routes import index


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SUIKA_DB')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.register_blueprint(index.blueprint)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return app


def scr():
    scraper = BeerScrape()
    data = scraper.scrape()

    for d in data:
        print(d)
        print()
