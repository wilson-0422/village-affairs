from datetime import datetime
from app import db


class Asset(db.Model):
    __tablename__ = 'assets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    location = db.Column(db.String(200))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='在用')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
