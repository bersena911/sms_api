from flask import jsonify

from exceptions.exceptions import MainException


def handle_unexpected_error(error):
    response = {
        'type': 'UnexpectedException',
        'message': 'An unexpected error has occurred.'
    }

    return jsonify(response), 500


def handle_error(error):
    response = {
        'message': error.message
    }

    return jsonify(response), error.status_code


error_handlers = (
    (Exception, handle_unexpected_error),
    (MainException, handle_error)
)
