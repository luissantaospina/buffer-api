from flask import Blueprint, jsonify

api_routes = Blueprint('api', __name__)


@api_routes.route('/insert', methods=['POST'])
def get_source_and_content():
    return jsonify({}), 200
