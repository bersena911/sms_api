import os

import dotenv

dotenv.load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
APP_ENV = os.environ.get('APP_ENV')
