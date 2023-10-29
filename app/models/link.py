from app.extensions import db
from datetime import datetime


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    personal_info = db.relationship('PersonalInfo', uselist=False, backref='link')
    token = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
