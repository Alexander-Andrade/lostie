from flask import render_template, request, redirect, url_for

from app.auth.decorators import login_required
from app.auth.helpers import get_current_user
from app.forms.personal_info_form import PersonalInfoForm
from app.models.link import Link
from app.models.personal_info import PersonalInfo
from app.extensions import db
from app.personal_info import personal_blueprint


@personal_blueprint.route('/info/<token>/details')
def personal_info_details(token):
    link = Link.query.filter_by(token=token).first()
    current_user = get_current_user()
    return render_template('personal_info/details.html', token=token, link=link,
                           current_user=current_user, personal_info=link.personal_info)


@personal_blueprint.route('/info/<token>/edit')
@login_required
def personal_info_edit(token):
    link = Link.query.filter_by(token=token).first()
    form = PersonalInfoForm(obj=link.personal_info)
    current_user = get_current_user()

    return render_template('personal_info/edit.html', token=token, form=form, current_user=current_user)


@personal_blueprint.route('/info/<token>/edit', methods=['POST'])
@login_required
def personal_info_post(token):
    form = PersonalInfoForm(request.form)

    if not form.validate():
        return render_template('personal_info/personal_info_edit.html', token=token, form=form)

    link = Link.query.filter_by(token=token).first()
    current_user = get_current_user()
    personal_info = link.personal_info or PersonalInfo()

    form.populate_obj(personal_info)

    if not personal_info.user:
        personal_info.user = current_user
    if not personal_info.link:
        personal_info.link = link

    db.session.add(personal_info)
    db.session.commit()

    return redirect(url_for('personal_info.personal_info_details', token=token))
