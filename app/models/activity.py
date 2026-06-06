from datetime import datetime
from app import db


class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    activity_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(200))
    organizer = db.Column(db.String(50))
    participants_count = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default='筹备中')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
