from flask import render_template, jsonify, request, redirect, url_for, flash
from flask_login import login_required ,login_user, logout_user
from flask.views import MethodView
from .models import User, Server, Service, db
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

    def _add_node(content):
        name = content.get('name')
        host = content.get('host')
        process_num = content.get('processNum')
        services = content.get('services')
        if name and host and process_num:
            try:
                node = Server(host=host, name=name, process_num=process_num)
                node.services = Service.query.filter(Service.name.in_(services)).all()
                db.session.add(node)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'

    def _add_service(content):
        name = content.get('name')
        slug = content.get('slug')
        port = content.get('port')
        servers = content.get('servers')
        if name and slug and port:
            try:
                service = Service(name=name, port=port, slug=slug)
                service.servers = Server.query.filter(Server.name.in_(servers)).all()
                db.session.add(service)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'
    
    def _edit_node(content):
        id = content.get('id')
        name = content.get('name')
        host = content.get('host')
        process_num = content.get('processNum')
        services = content.get('services')
        if id and name and host and process_num:
            try:
                node = Server.query.filter_by(id=id).first()
                node.host=host
                node.name=name
                node.process_num=process_num
                node.services = Service.query.filter(Service.name.in_(services)).all()
                db.session.add(node)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'
    
    def _edit_service(content):
        id = content.get('id')
        name = content.get('name')
        slug = content.get('slug')
        port = content.get('port')
        servers = content.get('servers')
        if id and name and slug and port:
            try:
                service = Service.query.filter_by(id=id).first()
                service.name=name
                service.port=port
                service.slug=slug
                service.servers = Server.query.filter(Server.name.in_(servers)).all()
                db.session.add(service)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'
    
    def _delete_node(content):
        id = content.get('id')
        if id:
            try:
                node = Server.query.filter_by(id=id).first()
                node.services = []
                db.session.delete(node)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'
    
    def _delete_service(content):
        id = content.get('id')
        if id:
            try:
                service = Service.query.filter_by(id=id).first()
                service.servers = []
                db.session.delete(service)
                db.session.commit()
                return True, 'ok'
            except Exception as e:
                db.session.rollback()
                return False, str(e)
        else:
            return False, 'parameter error'
    
    _action_map = {
        'add-node': _add_node,
        'add-service': _add_service,
        'edit-node': _edit_node,
        'edit-service': _edit_service,
        'delete-node': _delete_node,
        'delete-service': _delete_service
    }

    def get(self):
        servers = Server.query.all()
        services = Service.query.all()
        return render_template('index.html', **locals())
    
    def post(self):
        data = json.loads(str(request.data, encoding='utf-8'))
        action = data.get('action')
        ttype = data.get('type')
        content = data.get('content')
        if action and ttype and content:
            action_func = self._action_map.get('-'.join([action, ttype]))
            if action_func:
                result = action_func(content)
                if result[0]:
                    return jsonify({'code': 200, 'msg': result[1]}), 200
                else:
                    return jsonify({'code': 403, 'msg': result[1]}), 403
        return jsonify({'code': 401, 'msg': 'parameter error'}), 401
    
