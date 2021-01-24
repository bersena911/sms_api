import json
from typing import List

import requests
from lxml import html

from models.lambda_response import LambdaResponse


class MagtiFunService:
    _csrf_token = None

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self._session = requests.Session()
        self._update_auth_token()

    def _update_auth_token(self) -> None:
        first_page = 'http://www.magtifun.ge/index.php?page=1&lang=ge'

        response = self._session.get(first_page)
        page = response.text.encode('utf-8')
        html_response = html.fromstring(page)
        token = html_response.xpath('//input[@name="csrf_token"]/@value')
        self._csrf_token = token[0]

        login_url = 'http://www.magtifun.ge/index.php?page=11&lang=ge'
        data = {
            'csrf_token': self._csrf_token,
            'act': '1',
            'user': self.username,
            'password': self.password
        }
        response = self._session.post(login_url, data=data)
        page = response.text.encode('utf-8')
        html_response = html.fromstring(page)
        user_input = html_response.xpath('//input[@id="user"]')
        if user_input:
            raise Exception('Incorrect Credentials')

    def send_message(self, message: str, numbers: List[str]) -> requests.Response:
        send_url = 'http://www.magtifun.ge/scripts/sms_send.php'
        data = {
            'csrf_token': self._csrf_token,
            'recipients': ','.join(numbers),
            'total_recipients': len(numbers),
            'message_body': message
        }
        headers = {
            'Referer': 'http://www.magtifun.ge/index.php?page=2&lang=ge',
        }

        response = self._session.post(send_url, data=data, headers=headers)
        return response


def lambda_handler(event: dict, context: dict) -> dict:
    payload = event['body']
    if isinstance(payload, str):
        payload = json.loads(payload)
    username = payload['username']
    password = payload['password']
    message = payload['message']
    numbers = payload['numbers']
    try:
        magtifun = MagtiFunService(username=username, password=password)
        response = magtifun.send_message(message, numbers)
        status_code = response.status_code
    except Exception:
        status_code = 401

    return LambdaResponse(statusCode=status_code).__dict__
