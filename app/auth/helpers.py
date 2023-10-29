from flask import session

from app.models.user import User


def get_current_user():
    user_id = session.get('user_id')

    return User.query.get(user_id) if user_id is not None else None
