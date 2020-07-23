from flask import Blueprint
from suika.models.product import Product
from suika.models.price import Price

blueprint = Blueprint('product', __name__)


@blueprint.route('/')
def index() -> dict:
    return Product.query.all()
