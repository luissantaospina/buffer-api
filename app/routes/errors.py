from flask import jsonify, Blueprint, Response
from ..exceptions import UnsupportedPolicy, EmptyBuffer

errors_scope = Blueprint("errors", __name__)


def __generate_error_response(error: Exception) -> Response:
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    return jsonify(message)


def __generate_info_response(info: Exception) -> Response:
    message = {
        "InfoType": type(info).__name__,
        "Message": str(info)
    }
    return jsonify(message)


@errors_scope.app_errorhandler(UnsupportedPolicy)
def handle_user_not_found(error: UnsupportedPolicy) -> Response:
    response = __generate_error_response(error)
    response.status_code = 422
    return response


@errors_scope.app_errorhandler(EmptyBuffer)
def handle_user_not_found(info: EmptyBuffer) -> Response:
    response = __generate_info_response(info)
    response.status_code = 200
    return response
