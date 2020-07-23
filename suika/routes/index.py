from flask import Blueprint

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index() -> dict:
    return {
        'name': 'Suika',
        'version': '0.1'
    }
