import yaml
import os


class Configuration:

    def __init__(self, *args, **kwargs):
        super(Configuration, self).__init__(*args, **kwargs)

        with open('configs/magtifun.yaml', 'r') as config_yaml:
            '''
            Creating configurations from yaml
            '''
            yaml_file = yaml.safe_load(config_yaml)
            self.magti_login_data = dict(user=os.environ.get('MAGTIFUN_USER'), password=os.environ.get('MAGTIFUN_PASSWORD'))
            self.magti_cookies = yaml_file['magti_cookies']
            self.magti_headers = yaml_file['magti_headers']
            data = yaml_file['magti_data']
            self.magti_data = [tuple(x) for x in data]
