from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.notice_service import NoticeService

notices_bp = Blueprint('notices', __name__, url_prefix='/notices')


@notices_bp.route('/')
@login_required
def list_notices():
    notices = NoticeService.get_all()
    return render_template('notices/list.html', notices=notices)


@notices_bp.route('/<int:notice_id>')
@login_required
def detail(notice_id):
    notice = NoticeService.get_by_id(notice_id)
    if not notice:
        flash('公示不存在', 'danger')
        return redirect(url_for('notices.list_notices'))
    return render_template('notices/detail.html', notice=notice)


@notices_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        from datetime import datetime
        data = {
            'title': request.form.get('title'),
            'content': request.form.get('content'),
            'category': request.form.get('category'),
            'publisher': request.form.get('publisher'),
            'publish_date': datetime.strptime(request.form.get('publish_date'), '%Y-%m-%d').date() if request.form.get('publish_date') else None,
            'status': request.form.get('status', '草稿')
        }
        NoticeService.create(**data)
        flash('公示创建成功', 'success')
        return redirect(url_for('notices.list_notices'))
    return render_template('notices/create.html')


@notices_bp.route('/<int:notice_id>/publish', methods=['POST'])
@login_required
def publish(notice_id):
    notice = NoticeService.publish(notice_id)
    if notice:
        flash('公示发布成功', 'success')
    else:
        flash('公示发布失败', 'danger')
    return redirect(url_for('notices.detail', notice_id=notice_id))


@notices_bp.route('/<int:notice_id>/delete', methods=['POST'])
@login_required
def delete(notice_id):
    if NoticeService.delete(notice_id):
        flash('公示删除成功', 'success')
    else:
        flash('公示删除失败', 'danger')
    return redirect(url_for('notices.list_notices'))
