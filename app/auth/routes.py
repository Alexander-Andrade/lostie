from flask import render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth import auth_blueprint
from app.auth.decorators import login_required
from app.forms.login_form import LoginForm
from app.forms.signup_form import SignupForm
from app.models.user import User
from app.models.link import Link
from app.extensions import db


@auth_blueprint.route('/smartshield/<token>')
def smartshield(token):
    link = Link.query.filter_by(token=token).first()

    if not link:
        return render_template('link_not_found.html')
    if not link.personal_info and 'user_id' not in session:
        return redirect(url_for('auth.signup', token=token))
    elif not link.personal_info and 'user_id' in session:
        return redirect(url_for('personal_info.personal_info_edit', token=token))
    else:
        return redirect(url_for('personal_info.personal_info_details', token=token))


@auth_blueprint.route('/signup/<token>')
def signup(token):
    form = SignupForm()

    return render_template('auth/signup.html', token=token, form=form)


@auth_blueprint.route('/signup/<token>', methods=['POST'])
def signup_post(token):
    form = SignupForm(request.form)

    if not form.validate():
        return render_template('auth/signup.html', token=token, form=form)

    user = User(email=form.email.data, name=form.name.data, password=generate_password_hash(form.password.data))
    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id

    return redirect(url_for('personal_info.personal_info_edit', token=token))


@auth_blueprint.route('/login/<token>')
def login(token):
    form = LoginForm()

    return render_template('auth/login.html', token=token, form=form)


@auth_blueprint.route('/login/<token>', methods=['POST'])
def login_post(token):
    form = LoginForm(request.form)

    if not form.validate():
        return render_template('auth/login.html', token=token, form=form)

    link = Link.query.filter_by(token=token).first()
    user = User.query.filter_by(email=form.email.data).first()

    if not user or not check_password_hash(user.password, form.password.data):
        return redirect(url_for('auth.login'))

    session['user_id'] = user.id

    if not link.personal_info:
        return redirect(url_for('personal_info.personal_info_edit', token=token))
    else:
        return redirect(url_for('personal_info.personal_info_details', token=token))


@auth_blueprint.route('/logout/<token>')
def logout(token):
    session.pop('user_id')
    return redirect(url_for('personal_info.personal_info_details', token=token))


@auth_blueprint.route('/logout')
@login_required
def logout_without_token():
    session.pop('user_id')
    return redirect(url_for('auth.logged_out'))


@auth_blueprint.route('/logged_out')
def logged_out():
    return render_template('auth/logged_out.html')
