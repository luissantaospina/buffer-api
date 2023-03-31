from flask import Blueprint, request
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.validators import validate_policy
from app.controllers import buffer_controller

api_routes = Blueprint('api', __name__)


@api_routes.route('/insert', methods=['POST'])
def insert_item_to_buffer():
    data_inserted = buffer_controller.insert_item_to_buffer(MessageDTO(request.json['message']))
    return {'result': 'the data has been inserted successfully', 'message': data_inserted}, 201


@api_routes.route('/extract', methods=['POST'])
def extract_item_to_buffer():
    validate_policy(PolicyDTO(request.json['policy']))
    buffer_controller.extract_item_to_buffer(PolicyDTO(request.json['policy']))
    return '', 204


@api_routes.route('/', methods=['GET'])
def get_buffer():
    current_buffer = buffer_controller.get_all_buffer()
    return {'buffer': current_buffer}, 200
