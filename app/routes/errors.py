from flask import jsonify, Blueprint, Response
from ..exceptions import UnsupportedPolicy

errors_scope = Blueprint("errors", __name__)


def __generate_error_response(error: Exception) -> Response:
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    return jsonify(message)


@errors_scope.app_errorhandler(UnsupportedPolicy)
def handle_user_not_found(error: UnsupportedPolicy) -> Response:
    response = __generate_error_response(error)
    response.status_code = 422
    return response
