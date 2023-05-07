from flask import Flask, request, Response
from .extensions import db, restfulapi, cors, redis_store, limiter, bcrypt, login_manager
from .middleware import init_middleware
from .api.endpoints.user import user_bp
from .views import LoginView, IndexView
from .route import Route
from .balancer import Balancer
from utils.auth import Auth
import requests


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # 初始化中间件
    init_middleware(app)

    # 初始化扩展
    db.init_app(app)
    redis_store.init_app(app)
    restfulapi.init_app(app)
    cors.init_app(app)
    limiter.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # 注册 Blueprint
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

app = create_app()

with app.app_context():
    auth = Auth(app.config['ENCRYPTION'])
    balancer = Balancer(app.config['BALANCE_MODE'])

app.add_url_rule('/login', view_func=LoginView.as_view('login'))
app.add_url_rule('/index', view_func=IndexView.as_view('index'))

# 添加请求转发和负载均衡
@app.before_request
def before_request():
    # request.headers.add('X-Forwarded-For', request.remote_addr)
    response = None
    app_route = Route()
    slug = app_route.get_slug(request.url)
    if app_route.check_route(request.url):
        token = request.args.get('token', '')
        timestamp = request.args.get('timestamp', '')
        signature = request.args.get('signature', '')
        if auth.authentication(token,timestamp, signature):
            balancer.set_service_by_slug(slug)
            server = balancer.get_server()
            try:
                print('http://' + server + '/' + app_route.get_path(request.url))
                response = requests.request(
                    method=request.method,
                    url='http://' + server + '/' + app_route.get_path(request.url),
                    headers=request.headers,
                    data=request.get_data(),
                    cookies=request.cookies,
                    allow_redirects=False,
                )
            except Exception as e:
                print(e)
    if response is not None:
        resp = Response(response.content, status=response.status_code)
        resp.headers['content-type'] = response.headers['content-type']
        print(resp)
        return resp