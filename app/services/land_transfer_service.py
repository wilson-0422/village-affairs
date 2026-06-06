from app import db
from app.models.land_transfer import LandTransfer


class LandTransferService:
    @staticmethod
    def get_all():
        return LandTransfer.query.order_by(LandTransfer.created_at.desc()).all()

    @staticmethod
    def get_by_id(transfer_id):
        return LandTransfer.query.get(transfer_id)

    @staticmethod
    def get_by_status(status):
        return LandTransfer.query.filter_by(status=status).all()

    @staticmethod
    def create(**kwargs):
        transfer = LandTransfer(**kwargs)
        db.session.add(transfer)
        db.session.commit()
        return transfer

    @staticmethod
    def update(transfer_id, **kwargs):
        transfer = LandTransfer.query.get(transfer_id)
        if not transfer:
            return None
        for key, value in kwargs.items():
            if hasattr(transfer, key):
                setattr(transfer, key, value)
        db.session.commit()
        return transfer

    @staticmethod
    def delete(transfer_id):
        transfer = LandTransfer.query.get(transfer_id)
        if transfer:
            db.session.delete(transfer)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_type_stats():
        from sqlalchemy import func
        results = db.session.query(
            LandTransfer.transfer_type,
            func.count(LandTransfer.id).label('count'),
            func.sum(LandTransfer.area).label('total_area'),
            func.sum(LandTransfer.price).label('total_price')
        ).group_by(LandTransfer.transfer_type).all()
        return results
