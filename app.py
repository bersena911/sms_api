import logging

from flask import Flask, request, jsonify

from magtifun.magtifun import MagtiFun

app = Flask(__name__)
magtifun = MagtiFun()


@app.before_first_request
def init():
    logging.basicConfig(filename='logs.txt', level=logging.DEBUG)


@app.route('/', methods=['POST'])
def send():
    '''
    Sends message to given numbers.
    :return: Status response
    '''
    data = request.get_json()
    numbers = data['numbers']
    message = data['message']
    if not isinstance(numbers, list):
        return 500
    response = magtifun.send_message(message, numbers)
    return jsonify({'status': response.reason})
