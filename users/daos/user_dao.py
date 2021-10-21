from users.models.user import User
from app import db


def add_user(name, mail):
    if get_user_by_name(name) is not None:
        raise ValueError(f'User with name {name} already in the DB')

    user = User(username=name, email=mail)
    db.session.add(user)
    db.session.commit()


def get_user_by_name(name):
    return User.query.filter_by(username=name).first()


