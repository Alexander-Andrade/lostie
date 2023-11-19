from flask import render_template

from app.extensions import db
from app.auth.decorators import login_required
from app.auth.helpers import get_current_user
from app.models.link import Link
from app.models.personal_info import PersonalInfo
from app.products import products_blueprint


@products_blueprint.route('/products')
@login_required
def list():
    current_user = get_current_user()
    personal_infos = (PersonalInfo.query.join(Link).options(db.joinedload(PersonalInfo.link)).
                      filter(PersonalInfo.user_id == current_user.id).all())
    return render_template('products/list.html', current_user=current_user, personal_infos=personal_infos)
