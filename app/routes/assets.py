from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.asset_service import AssetService

assets_bp = Blueprint('assets', __name__, url_prefix='/assets')


@assets_bp.route('/')
@login_required
def list_assets():
    assets = AssetService.get_all()
    return render_template('assets/list.html', assets=assets)


@assets_bp.route('/<int:asset_id>')
@login_required
def detail(asset_id):
    asset = AssetService.get_by_id(asset_id)
    if not asset:
        flash('资产不存在', 'danger')
        return redirect(url_for('assets.list_assets'))
    return render_template('assets/detail.html', asset=asset)


@assets_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'category': request.form.get('category'),
            'value': float(request.form.get('value', 0)),
            'quantity': int(request.form.get('quantity', 1)),
            'location': request.form.get('location'),
            'description': request.form.get('description'),
            'status': request.form.get('status', '在用')
        }
        AssetService.create(**data)
        flash('资产创建成功', 'success')
        return redirect(url_for('assets.list_assets'))
    return render_template('assets/create.html')


@assets_bp.route('/<int:asset_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(asset_id):
    asset = AssetService.get_by_id(asset_id)
    if not asset:
        flash('资产不存在', 'danger')
        return redirect(url_for('assets.list_assets'))
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'category': request.form.get('category'),
            'value': float(request.form.get('value', 0)),
            'quantity': int(request.form.get('quantity', 1)),
            'location': request.form.get('location'),
            'description': request.form.get('description'),
            'status': request.form.get('status')
        }
        AssetService.update(asset_id, **data)
        flash('资产更新成功', 'success')
        return redirect(url_for('assets.detail', asset_id=asset_id))
    return render_template('assets/edit.html', asset=asset)


@assets_bp.route('/<int:asset_id>/delete', methods=['POST'])
@login_required
def delete(asset_id):
    if AssetService.delete(asset_id):
        flash('资产删除成功', 'success')
    else:
        flash('资产删除失败', 'danger')
    return redirect(url_for('assets.list_assets'))
