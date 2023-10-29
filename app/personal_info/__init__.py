from flask import Blueprint

personal_blueprint = Blueprint('personal_info', __name__)

from app.personal_info import routes