from .extensions import db
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime
from hashlib import md5
from enum import Enum
import uuid
import shortuuid


class Permissions(Enum):
    USER = 0
    CONTRIBUTOR = 50
    MANAGER = 70
    ADMIN = 99

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False
    
    def __le__(self, other):
        if self.value <= other.value:
            return True
        return False
    
    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False
    
    def __ge__(self, other):
        if self.value >= other.value:
            return True
        return False


class User(db.Model, UserMixin):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum(Permissions), default=Permissions.USER)
    token = db.Column(db.String(32), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, email, password):
        self.id = shortuuid.encode(uuid.uuid4())
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
    name = db.Column(db.String(50), nullable=False)
    host = db.Column(db.String(16), nullable=False)
    process_num = db.Column(db.Integer, nullable=False)
    services = db.relationship('Service', secondary='server_services', back_populates="server")

    def __init__(self, host, name, process_num):
        self.id = shortuuid.encode(uuid.uuid4())
        self.host = host
        self.name = name
        self.process_num = process_num
    
    def get_service_string(self):
        return '、'.join([service.name for service in self.services])


class Service(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(16), nullable=False)
    servers = db.relationship('Server', secondary='server_services', back_populates="service")

    def __init__(self, name, slug, port):
        self.id = shortuuid.encode(uuid.uuid4())
        self.name = name
        self.slug = slug
        self.port = port

    def get_server_string(self):
        return '、'.join([server.name for server in self.servers])


class ServerService(db.Model):
    __tablename__ = 'server_services'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.String(32), db.ForeignKey('server.id'))
    service_id = db.Column(db.String(32), db.ForeignKey('service.id'))
