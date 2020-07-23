from suika.models.db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    date_on_market = db.Column(db.Date, nullable=False)
    season = db.Column(db.String, nullable=False)
    prices = db.relationship('Price', backref='product')

    def add(self) -> None:
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f"<Product {self.id} - {self.name}>"
