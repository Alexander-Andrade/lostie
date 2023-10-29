from app.extensions import db
from datetime import datetime


class PersonalInfo(db.Model):
    __tablename__ = 'personal_infos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    contact_name = db.Column(db.String(64), nullable=False)
    contact_phone = db.Column(db.String(64), nullable=False)
    extra_contact_name = db.Column(db.String(64))
    extra_contact_phone = db.Column(db.String(64))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
