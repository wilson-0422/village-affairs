from datetime import datetime
from app import db


class Notice(db.Model):
    __tablename__ = 'notices'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50))
    publish_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='草稿')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
