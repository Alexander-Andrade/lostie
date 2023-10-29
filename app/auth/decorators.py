from functools import wraps
from flask import session, redirect, url_for, request


def login_required(view_func):
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if 'user_id' in session:
            return view_func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login', token=kwargs['token'], next=request.url))
    return decorated_view
