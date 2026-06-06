from app import db
from app.models.activity import Activity


class ActivityService:
    @staticmethod
    def get_all():
        return Activity.query.order_by(Activity.created_at.desc()).all()

    @staticmethod
    def get_by_id(activity_id):
        return Activity.query.get(activity_id)

    @staticmethod
    def get_upcoming():
        from datetime import date
        return Activity.query.filter(Activity.activity_date >= date.today()).order_by(Activity.activity_date).all()

    @staticmethod
    def create(**kwargs):
        activity = Activity(**kwargs)
        db.session.add(activity)
        db.session.commit()
        return activity

    @staticmethod
    def update(activity_id, **kwargs):
        activity = Activity.query.get(activity_id)
        if not activity:
            return None
        for key, value in kwargs.items():
            if hasattr(activity, key):
                setattr(activity, key, value)
        db.session.commit()
        return activity

    @staticmethod
    def delete(activity_id):
        activity = Activity.query.get(activity_id)
        if activity:
            db.session.delete(activity)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_status_stats():
        from sqlalchemy import func
        results = db.session.query(
            Activity.status,
            func.count(Activity.id).label('count')
        ).group_by(Activity.status).all()
        return results
