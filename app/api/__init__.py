from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix="/api")

# NOTE: Needed at the bottom to avoid circular dependecy errors
# http://flask.pocoo.org/docs/1.0/patterns/packages/
from . import routes # noqa
