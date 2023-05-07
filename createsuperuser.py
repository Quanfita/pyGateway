from app import create_app
from app.extensions import db
from app.models import User, Permissions

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        username = input('username: ')
        email = input('email: ')
        password = input('password: ')
        user = User(name=username, email=email, password=password)
        user.role = Permissions.ADMIN
        db.session.add(user)
        db.session.commit()
        print('token: ' + user.token)
