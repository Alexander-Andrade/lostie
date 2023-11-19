from flask import session

from app.models.user import User


def get_current_user():
    user_id = session.get('user_id')

    return User.query.get(user_id) if user_id is not None else None


def is_link_authorized(link, current_user):
    if not current_user:
        return False

    if not link.personal_info:
        return True

    return link.personal_info.user == current_user
