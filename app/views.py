from flask import render_template, jsonify, request, redirect, url_for, flash
from flask_login import login_required ,login_user, logout_user
from flask.views import MethodView
from .models import User
from app import login_manager
import json


@login_manager.user_loader
def get_user_by_id(id):
    # 从数据库获取用户对象
    return User.query.filter_by(id=id).first()

class LoginView(MethodView):
    def get(self):
        return render_template('login.html')
    
    def post(self):
        data = json.loads(str(request.data, encoding='utf-8'))
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(name=username).first()
        if user.authenticate(password):
            login_user(user, remember=True)
            return jsonify({'code': 200, 'msg': 'ok'}), 200
        else:
            return jsonify({'code': 401, 'msg': 'error'}), 401


class IndexView(MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('index.html')
