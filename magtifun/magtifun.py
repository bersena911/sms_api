import lxml.html
import requests

from configs.config import Configuration


class MagtiFun(Configuration):

    def __init__(self, *args, **kwargs):
        super(MagtiFun, self).__init__(*args, **kwargs)

    def send_message(self, message, numbers):
        '''
        Sends message to given numbers.
        :param message: Text to be sent.
        :param numbers: Receivers numbers.
        :return: Status response
        '''

        # Initialize urls
        first_page = 'http://www.magtifun.ge/index.php?page=1&lang=ge'
        login_url = 'http://www.magtifun.ge/index.php?page=11&lang=ge'
        post_url = 'http://www.magtifun.ge/scripts/sms_send.php'

        # Create MagtiFun session
        session = requests.Session()
        first_resp = session.get(first_page)
        page = first_resp.text.encode('utf-8')
        html = lxml.html.fromstring(page)
        token = html.xpath('//input[@name="csrf_token"]/@value')
        self.magti_login_data['csrf_token'] = token[0]

        # Get user cookies
        session.post(login_url, data=self.magti_login_data)
        User = session.cookies['User']
        self.magti_cookies['User'] = User

        # Initialize message
        self.magti_data.append(('csrf_token', token[0]))
        self.magti_data.append(('recipients', ','.join(numbers)))
        self.magti_data.append(('total_recipients', len(numbers)))
        self.magti_data.append(('message_body', message))

        # Use MagtiFun to send message
        response = session.post(post_url,
                                headers=self.magti_headers, cookies=self.magti_cookies, data=self.magti_data)
        return response
