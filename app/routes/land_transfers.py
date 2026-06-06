from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.land_transfer_service import LandTransferService

land_transfers_bp = Blueprint('land_transfers', __name__, url_prefix='/land-transfers')


@land_transfers_bp.route('/')
@login_required
def list_transfers():
    transfers = LandTransferService.get_all()
    return render_template('land_transfers/list.html', transfers=transfers)


@land_transfers_bp.route('/<int:transfer_id>')
@login_required
def detail(transfer_id):
    transfer = LandTransferService.get_by_id(transfer_id)
    if not transfer:
        flash('流转记录不存在', 'danger')
        return redirect(url_for('land_transfers.list_transfers'))
    return render_template('land_transfers/detail.html', transfer=transfer)


@land_transfers_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        from datetime import datetime
        data = {
            'land_location': request.form.get('land_location'),
            'area': float(request.form.get('area', 0)),
            'transfer_type': request.form.get('transfer_type'),
            'from_party': request.form.get('from_party'),
            'to_party': request.form.get('to_party'),
            'price': float(request.form.get('price', 0)),
            'start_date': datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date(),
            'end_date': datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date(),
            'status': request.form.get('status', '待审批'),
            'description': request.form.get('description')
        }
        LandTransferService.create(**data)
        flash('土地流转登记成功', 'success')
        return redirect(url_for('land_transfers.list_transfers'))
    return render_template('land_transfers/create.html')


@land_transfers_bp.route('/<int:transfer_id>/delete', methods=['POST'])
@login_required
def delete(transfer_id):
    if LandTransferService.delete(transfer_id):
        flash('流转记录删除成功', 'success')
    else:
        flash('流转记录删除失败', 'danger')
    return redirect(url_for('land_transfers.list_transfers'))
