from flask import Flask, request, jsonify

from exceptions.handlers import error_handlers
from models.requests.message_payload import MessagePayload
from services.magtifun_service import MagtiFunService

app = Flask(__name__)

for error_handler in error_handlers:
    app.register_error_handler(*error_handler)


@app.route('/', methods=['POST'])
def send():
    data = request.get_json()

    validator_response = MessagePayload().validate(data)
    if validator_response:
        return jsonify(validator_response)

    username = data['username']
    password = data['password']
    numbers = data['numbers']
    message = data['message']

    magtifun = MagtiFunService(username=username, password=password)

    response = magtifun.send_message(message, numbers)

    return jsonify({'status': response.reason})
