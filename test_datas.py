from app import create_app
from app.extensions import db
from app.models import Server, Service

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        server = Server(host='127.0.0.1', port=8001, process_num=2)
        service = Service('test', 'test')
        service.servers.append(server)
        # server.services.append(service)
        db.session.add(server)
        db.session.add(service)
        db.session.commit()
