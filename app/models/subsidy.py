from datetime import datetime
from app import db


class Subsidy(db.Model):
    __tablename__ = 'subsidies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    total_budget = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    distributions = db.relationship('SubsidyDistribution', backref='subsidy', lazy=True)


class SubsidyDistribution(db.Model):
    __tablename__ = 'subsidy_distributions'

    id = db.Column(db.Integer, primary_key=True)
    subsidy_id = db.Column(db.Integer, db.ForeignKey('subsidies.id'), nullable=False)
    villager_name = db.Column(db.String(50), nullable=False)
    id_card = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='待发放')
    distributed_at = db.Column(db.DateTime)
