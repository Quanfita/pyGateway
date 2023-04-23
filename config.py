import os

BASE_DIR = os.path.dirname(__file__)

# Flask Setting
DEBUG = True
TESTING = False
SECRET_KEY = 'your_secret_key'
JSON_SORT_KEYS = False

# Database Setting
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT Setting
JWT_SECRET_KEY = 'your_jwt_secret_key'
JWT_TOKEN_LOCATION = ['headers', 'cookies']
JWT_ACCESS_TOKEN_EXPIRES = 3600

# Log Setting
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'app.log'
LOGGING_LEVEL = 'INFO'

# Run Setting

# Port to listen on
LISTEN_PORT =  5000

# API method, optional POST, GET and MIXED. 
# Note that if you choose to MIXED, you need to manually configure
# the method when configuring the api parameters
METHOD = 'POST'

# Authentication method, optional token, token-secret,
# token-signature, token-secret-signature
AUTH_METHOD = 'token-signature'

# Authentication encryption method, optional md5, sha256
ENCRYPTION = 'sha256'

# Data transmission method, optional args, form, json. 
# We recommend using json. Note that if you choose form and json, 
# please choose the POST method when configuring the API method.
TRANSMISSION_METHOD = 'json'

# Load balancing mode, including random, cycle, random-weight, 
# cycle-weight four modes
BALANCE_MODE = 'random'