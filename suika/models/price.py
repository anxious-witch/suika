from suika.models.base import Base
from suika.models.db import db


class Price(Base):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', back_populates='prices')
    price = db.Column(db.Integer, nullable=False)

    def serialize(self) -> dict:
        return {
            'price': self.price,
            'date_created': self.date_created
        }

    def __repr__(self) -> str:
        return f"<Price {self.id} - {self.price}>"
