from app import db
from app.models.asset import Asset


class AssetService:
    @staticmethod
    def get_all():
        return Asset.query.order_by(Asset.created_at.desc()).all()

    @staticmethod
    def get_by_id(asset_id):
        return Asset.query.get(asset_id)

    @staticmethod
    def get_by_category(category):
        return Asset.query.filter_by(category=category).all()

    @staticmethod
    def get_by_status(status):
        return Asset.query.filter_by(status=status).all()

    @staticmethod
    def create(**kwargs):
        asset = Asset(**kwargs)
        db.session.add(asset)
        db.session.commit()
        return asset

    @staticmethod
    def update(asset_id, **kwargs):
        asset = Asset.query.get(asset_id)
        if not asset:
            return None
        for key, value in kwargs.items():
            if hasattr(asset, key):
                setattr(asset, key, value)
        db.session.commit()
        return asset

    @staticmethod
    def delete(asset_id):
        asset = Asset.query.get(asset_id)
        if asset:
            db.session.delete(asset)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_category_stats():
        from sqlalchemy import func
        results = db.session.query(
            Asset.category,
            func.count(Asset.id).label('count'),
            func.sum(Asset.value).label('total_value')
        ).group_by(Asset.category).all()
        return results

    @staticmethod
    def get_status_stats():
        from sqlalchemy import func
        results = db.session.query(
            Asset.status,
            func.count(Asset.id).label('count')
        ).group_by(Asset.status).all()
        return results
