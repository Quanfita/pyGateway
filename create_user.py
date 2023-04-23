from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        username = input('username: ')
        email = input('email: ')
        password = input('password: ')
        user = User(name=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print('token: ' + user.token)
