import os

import dotenv

dotenv.load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
