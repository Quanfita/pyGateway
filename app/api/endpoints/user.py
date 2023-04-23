from flask import Blueprint
from flask_restful import Resource, fields, marshal_with
from .auth import auth_required
from ...models import User

# 创建 API 端点
user_bp = Blueprint('user', __name__)

user = {
    'id': fields.Integer(),
    'name': fields.String(),
    'email': fields.String(),
}

@user_bp.route('/')
class UserList(Resource):
    @auth_required
    @marshal_with(user)
    def get(self):
        users = User.query.all()
        return users

@user_bp.route('/<int:user_id>')
class UserDetail(Resource):
    @auth_required
    @marshal_with(user)
    def get(self, user_id):
        user = User.query.get(user_id)
        return user