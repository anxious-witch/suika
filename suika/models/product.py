from suika.models.base import Base
from suika.models.db import db


class Product(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String, unique=True, index=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    abv = db.Column(db.Float, nullable=False)
    country_of_origin = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False)
    container_type = db.Column(db.String, nullable=False)
    style = db.Column(db.String, nullable=False)
    sub_style = db.Column(db.String, nullable=False)
    producer = db.Column(db.String, nullable=False)
    short_description = db.Column(db.Text)
    season = db.Column(db.String, nullable=False)
    prices = db.relationship('Price', back_populates='product')

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'sku': self.sku,
            'name': self.name,
            'volume': self.volume,
            'abv': self.abv,
            'country_of_origin': self.country_of_origin,
            'available': self.available,
            'container_type': self.container_type,
            'style': self.style,
            'sub_style': self.sub_style,
            'producer': self.producer,
            'short_description': self.short_description,
            'date_created': self.date_created,
            'season': self.season,
            'prices': [price.serialize() for price in self.prices]
        }

    def __repr__(self) -> str:
        return f"<Product {self.id} - {self.name}>"
