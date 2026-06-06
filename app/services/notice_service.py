from app import db
from app.models.notice import Notice


class NoticeService:
    @staticmethod
    def get_all():
        return Notice.query.order_by(Notice.created_at.desc()).all()

    @staticmethod
    def get_published():
        return Notice.query.filter_by(status='已发布').order_by(Notice.publish_date.desc()).all()

    @staticmethod
    def get_by_id(notice_id):
        return Notice.query.get(notice_id)

    @staticmethod
    def create(**kwargs):
        notice = Notice(**kwargs)
        db.session.add(notice)
        db.session.commit()
        return notice

    @staticmethod
    def update(notice_id, **kwargs):
        notice = Notice.query.get(notice_id)
        if not notice:
            return None
        for key, value in kwargs.items():
            if hasattr(notice, key):
                setattr(notice, key, value)
        db.session.commit()
        return notice

    @staticmethod
    def delete(notice_id):
        notice = Notice.query.get(notice_id)
        if notice:
            db.session.delete(notice)
            db.session.commit()
            return True
        return False

    @staticmethod
    def publish(notice_id):
        from datetime import date
        notice = Notice.query.get(notice_id)
        if notice:
            notice.status = '已发布'
            notice.publish_date = date.today()
            db.session.commit()
            return notice
        return None

    @staticmethod
    def get_category_stats():
        from sqlalchemy import func
        results = db.session.query(
            Notice.category,
            func.count(Notice.id).label('count')
        ).group_by(Notice.category).all()
        return results
