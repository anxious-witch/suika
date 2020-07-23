from suika.models.db import db


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', back_populates='prices')
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def serialize(self) -> dict:
        return {
            'price': self.price,
            'date': self.date
        }
