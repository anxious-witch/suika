from flask import Blueprint
from flask.json import jsonify
from suika.models.product import Product

blueprint = Blueprint('product', __name__, url_prefix='/product')


@blueprint.route('/')
def index() -> dict:
    products = [product.serialize() for product in Product.query.all()]
    return jsonify(products)


@blueprint.route('/<id>')
def product(id) -> dict:
    product = Product.query.get(id)
    return jsonify(product.serialize())
