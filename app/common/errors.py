from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException


def build_error_response(status_code, message):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


# TODO: Make this more granular
def configure_api_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exceptions(error):
        return build_error_response(error.code, error.description)
