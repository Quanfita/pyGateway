from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# 创建 CORS 扩展实例
cors = CORS(resources={r"/api/*": {"origins": "*"}}, expose_headers='Authorization')

# 创建 RESTful 扩展实例
restfulapi = Api()

# 创建 SQLAlchemy 扩展实例
db = SQLAlchemy()

# 创建 Redis 扩展实例
redis_store = FlaskRedis()

# 创建 Flask-Limiter 扩展实例
limiter = Limiter(key_func=get_remote_address)
