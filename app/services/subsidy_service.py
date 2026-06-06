from datetime import datetime
from app import db
from app.models.subsidy import Subsidy, SubsidyDistribution


class SubsidyService:
    @staticmethod
    def get_all():
        return Subsidy.query.order_by(Subsidy.created_at.desc()).all()

    @staticmethod
    def get_by_id(subsidy_id):
        return Subsidy.query.get(subsidy_id)

    @staticmethod
    def create(**kwargs):
        subsidy = Subsidy(**kwargs)
        db.session.add(subsidy)
        db.session.commit()
        return subsidy

    @staticmethod
    def delete(subsidy_id):
        subsidy = Subsidy.query.get(subsidy_id)
        if subsidy:
            db.session.delete(subsidy)
            db.session.commit()
            return True
        return False

    @staticmethod
    def distribute(subsidy_id, distributions):
        subsidy = Subsidy.query.get(subsidy_id)
        if not subsidy:
            return None
        for d in distributions:
            dist = SubsidyDistribution(
                subsidy_id=subsidy_id,
                villager_name=d['villager_name'],
                id_card=d['id_card'],
                amount=d.get('amount', subsidy.amount),
                status='待发放'
            )
            db.session.add(dist)
        db.session.commit()
        return subsidy

    @staticmethod
    def get_distributions(subsidy_id):
        return SubsidyDistribution.query.filter_by(subsidy_id=subsidy_id).all()

    @staticmethod
    def confirm_distribution(dist_id):
        dist = SubsidyDistribution.query.get(dist_id)
        if dist:
            dist.status = '已发放'
            dist.distributed_at = datetime.utcnow()
            db.session.commit()
            return dist
        return None

    @staticmethod
    def get_category_stats():
        from sqlalchemy import func
        results = db.session.query(
            Subsidy.category,
            func.count(Subsidy.id).label('count'),
            func.sum(Subsidy.total_budget).label('total_budget')
        ).group_by(Subsidy.category).all()
        return results
