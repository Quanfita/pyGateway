from flask_cors import CORS
from flask_jwt_extended import JWTManager


# 初始化跨域中间件
def init_cors(app):
    CORS(app)

# 初始化 JWT manager 中间件
def init_jwt_manager(app):
    jwt = JWTManager(app)
    return jwt

# 初始化所有中间件
def init_middleware(app):
    init_cors(app)
    init_jwt_manager(app)