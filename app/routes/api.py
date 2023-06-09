from flask import Blueprint, request
from app.data_transfer_objects import MessageDTO, PolicyDTO
from app.controllers import buffer_controller

api_routes = Blueprint('api', __name__)


@api_routes.route('/insert', methods=['POST'])
def insert_item_to_buffer():
    data_inserted = buffer_controller.insert_item_to_buffer(MessageDTO(request.json['message']))
    return {'result': 'the data has been inserted successfully', 'message': data_inserted.body}, 201


@api_routes.route('/extract', methods=['POST'])
def extract_item_to_buffer():
    data_extracted = buffer_controller.extract_item_to_buffer(PolicyDTO(request.json['policy']))
    return {'result': 'the data has been extracted successfully', 'message': data_extracted}, 200


@api_routes.route('/', methods=['GET'])
def get_buffer():
    current_buffer = buffer_controller.get_all_buffer()
    return {'buffer': current_buffer}, 200
