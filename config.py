import os

BASE_DIR = os.path.dirname(__file__)

# Flask配置
DEBUG = True
TESTING = False
SECRET_KEY = 'your_secret_key'
JSON_SORT_KEYS = False

# 数据库配置
SQLALCHEMY_DATABASE_URI = f'sqlite:///test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT配置
JWT_SECRET_KEY = 'your_jwt_secret_key'
JWT_TOKEN_LOCATION = ['headers', 'cookies']
JWT_ACCESS_TOKEN_EXPIRES = 3600

# 日志配置
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = 'app.log'
LOGGING_LEVEL = 'INFO'

# 其他配置

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


BALANCE_MODE = 'random'