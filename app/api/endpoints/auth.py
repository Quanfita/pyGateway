from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ...extensions import bcrypt
from ...models import User


# 用户注册
def register_user(name, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(name=name, email=email, password=hashed_password)
    user.save()
    return user

# 用户登录
def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.email)
        return {'access_token': access_token}, 200
    else:
        return {'message': 'Invalid email or password'}, 401

# 鉴权装饰器
def auth_required(func):
    @jwt_required()
    def wrapper(*args, **kwargs):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        if not user:
            return {'message': 'User not found'}, 401
        return func(user, *args, **kwargs)
    return wrapper
