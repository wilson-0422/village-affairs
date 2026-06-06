from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.activity_service import ActivityService

activities_bp = Blueprint('activities', __name__, url_prefix='/activities')


@activities_bp.route('/')
@login_required
def list_activities():
    activities = ActivityService.get_all()
    return render_template('activities/list.html', activities=activities)


@activities_bp.route('/<int:activity_id>')
@login_required
def detail(activity_id):
    activity = ActivityService.get_by_id(activity_id)
    if not activity:
        flash('活动不存在', 'danger')
        return redirect(url_for('activities.list_activities'))
    return render_template('activities/detail.html', activity=activity)


@activities_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        from datetime import datetime
        data = {
            'title': request.form.get('title'),
            'content': request.form.get('content'),
            'activity_date': datetime.strptime(request.form.get('activity_date'), '%Y-%m-%d').date(),
            'location': request.form.get('location'),
            'organizer': request.form.get('organizer'),
            'participants_count': int(request.form.get('participants_count', 0)),
            'status': request.form.get('status', '筹备中')
        }
        ActivityService.create(**data)
        flash('活动创建成功', 'success')
        return redirect(url_for('activities.list_activities'))
    return render_template('activities/create.html')


@activities_bp.route('/<int:activity_id>/delete', methods=['POST'])
@login_required
def delete(activity_id):
    if ActivityService.delete(activity_id):
        flash('活动删除成功', 'success')
    else:
        flash('活动删除失败', 'danger')
    return redirect(url_for('activities.list_activities'))
