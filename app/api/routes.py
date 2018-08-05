from flask import abort, jsonify, request
from . import api_blueprint as api
from .v1.valuation import calculate_valuation as calculate_valuation_v1


@api.route('/v1/valuation', methods=['POST'])
def return_valuation_v1():
    data = request.get_json()
    # NOTE: Temporary logic to be replaced by more robust validation
    if bool(data) is False:
        error_message = 'Empty data'
        abort(400, error_message)
    valuation = calculate_valuation_v1(data)
    return jsonify(valuation)
