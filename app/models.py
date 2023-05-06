from .extensions import db
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime
from hashlib import md5
import uuid

class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(32), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = generate_password_hash(password).decode('utf-8')
        self.token = md5(self.id.encode('utf-8')).hexdigest()
        self.create_time = datetime.now()
    
    def get_id(self):
        return self.id
    
    def authenticate(self, password):
        return check_password_hash(self.password, password)


class Server(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    host = db.Column(db.String(16), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    process_num = db.Column(db.Integer, nullable=False)
    services = db.relationship('Service', secondary='server_services')

    def __init__(self, host, port, process_num):
        self.id = str(uuid.uuid4())
        self.host = host
        self.port = port
        self.process_num = process_num


class Service(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(16), nullable=False)
    servers = db.relationship('Server', secondary='server_services')

    def __init__(self, name, slug):
        self.id = str(uuid.uuid4())
        self.name = name
        self.slug = slug


class ServerService(db.Model):
    __tablename__ = 'server_services'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.String(32), db.ForeignKey('server.id'))
    service_id = db.Column(db.String(32), db.ForeignKey('service.id'))
