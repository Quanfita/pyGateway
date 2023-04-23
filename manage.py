from app import app, db
from flask_migrate import Migrate
import platform

migrate = Migrate(app, db)

if __name__ == '__main__':
    system = platform.system()
    if system == 'Windows':
        app.run(host='0.0.0.0', port=app.config["LISTEN_PORT"], debug=app.config['DEBUG'])
    else:
        # 使用Gunicorn作为Web服务器启动应用程序
        from gunicorn.app.base import BaseApplication

        class FlaskApplication(BaseApplication):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super().__init__()

            def load_config(self):
                config = {
                    key: value for key, value in self.options.items()
                    if key in self.cfg.settings and value is not None
                }
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        options = {
            'bind': f'0.0.0.0:{app.config["LISTEN_PORT"]}',  # 绑定的地址和端口
            'workers': 4,  # 启动的worker进程数
        }
        FlaskApplication(app, options).run()