from suika.models.db import db
from sqlalchemy.sql import func


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', back_populates='prices')
    price = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    date_modified = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def serialize(self) -> dict:
        return {
            'price': self.price,
            'date_created': self.date_created
        }

    def __repr__(self) -> str:
        return f"<Price {self.id} - {self.price}>"
