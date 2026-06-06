from flask import Blueprint, render_template
from flask_login import login_required
from app.services.asset_service import AssetService
from app.services.land_transfer_service import LandTransferService
from app.services.subsidy_service import SubsidyService
from app.services.activity_service import ActivityService
from app.services.notice_service import NoticeService
from app.models.asset import Asset
from app.models.land_transfer import LandTransfer
from app.models.subsidy import Subsidy
from app.models.activity import Activity
from app.models.notice import Notice

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    published_notices = NoticeService.get_published()[:5]
    upcoming_activities = ActivityService.get_upcoming()[:5]
    return render_template('index.html', notices=published_notices, activities=upcoming_activities)


@main_bp.route('/dashboard')
@login_required
def dashboard():
    from app import db
    from sqlalchemy import func
    asset_count = Asset.query.count()
    asset_total_value = db.session.query(func.sum(Asset.value)).scalar() or 0
    transfer_count = LandTransfer.query.count()
    subsidy_count = Subsidy.query.count()
    activity_count = Activity.query.count()
    notice_count = Notice.query.count()
    category_stats = AssetService.get_category_stats()
    status_stats = AssetService.get_status_stats()
    transfer_type_stats = LandTransferService.get_type_stats()
    subsidy_category_stats = SubsidyService.get_category_stats()
    activity_status_stats = ActivityService.get_status_stats()
    notice_category_stats = NoticeService.get_category_stats()
    return render_template('dashboard/overview.html',
                           asset_count=asset_count,
                           asset_total_value=asset_total_value,
                           transfer_count=transfer_count,
                           subsidy_count=subsidy_count,
                           activity_count=activity_count,
                           notice_count=notice_count,
                           category_stats=category_stats,
                           status_stats=status_stats,
                           transfer_type_stats=transfer_type_stats,
                           subsidy_category_stats=subsidy_category_stats,
                           activity_status_stats=activity_status_stats,
                           notice_category_stats=notice_category_stats)
