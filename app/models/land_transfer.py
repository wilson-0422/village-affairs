from datetime import datetime
from app import db


class LandTransfer(db.Model):
    __tablename__ = 'land_transfers'

    id = db.Column(db.Integer, primary_key=True)
    land_location = db.Column(db.String(200), nullable=False)
    area = db.Column(db.Float, nullable=False)
    transfer_type = db.Column(db.String(20), nullable=False)
    from_party = db.Column(db.String(50), nullable=False)
    to_party = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='待审批')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
