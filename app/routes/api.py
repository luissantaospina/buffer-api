from flask import Blueprint, request
from app.services import buffer_service

api_routes = Blueprint('api', __name__)


@api_routes.route('/insert', methods=['POST'])
def insert_item_to_buffer():
    buffer_service.insert_item_to_buffer(request.json['message'])
    return '', 201


@api_routes.route('/extract', methods=['POST'])
def extract_item_to_buffer():
    buffer_service.extract_item_to_buffer(request.json['policy'])
    return '', 204


@api_routes.route('/', methods=['GET'])
def get_buffer():
    current_buffer = buffer_service.get_all_buffer()
    return {'buffer': current_buffer}, 200
