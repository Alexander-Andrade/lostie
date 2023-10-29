from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from app.personal_info import personal_blueprint
from app.auth import auth_blueprint
from app.extensions import db, migrate, csrf


def create_app(config_class=Config):
    app = Flask(__name__)

    # if app.config['FLASK_ENV'] == 'development':
    from dotenv import load_dotenv
    load_dotenv()

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(personal_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

