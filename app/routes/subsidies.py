from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.subsidy_service import SubsidyService

subsidies_bp = Blueprint('subsidies', __name__, url_prefix='/subsidies')


@subsidies_bp.route('/')
@login_required
def list_subsidies():
    subsidies = SubsidyService.get_all()
    return render_template('subsidies/list.html', subsidies=subsidies)


@subsidies_bp.route('/<int:subsidy_id>')
@login_required
def detail(subsidy_id):
    subsidy = SubsidyService.get_by_id(subsidy_id)
    if not subsidy:
        flash('补贴项目不存在', 'danger')
        return redirect(url_for('subsidies.list_subsidies'))
    distributions = SubsidyService.get_distributions(subsidy_id)
    return render_template('subsidies/detail.html', subsidy=subsidy, distributions=distributions)


@subsidies_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'category': request.form.get('category'),
            'amount': float(request.form.get('amount', 0)),
            'total_budget': float(request.form.get('total_budget', 0)),
            'description': request.form.get('description')
        }
        SubsidyService.create(**data)
        flash('补贴项目创建成功', 'success')
        return redirect(url_for('subsidies.list_subsidies'))
    return render_template('subsidies/create.html')


@subsidies_bp.route('/<int:subsidy_id>/distribute', methods=['GET', 'POST'])
@login_required
def distribute(subsidy_id):
    subsidy = SubsidyService.get_by_id(subsidy_id)
    if not subsidy:
        flash('补贴项目不存在', 'danger')
        return redirect(url_for('subsidies.list_subsidies'))
    if request.method == 'POST':
        names = request.form.getlist('villager_name')
        id_cards = request.form.getlist('id_card')
        amounts = request.form.getlist('amount')
        distributions = []
        for i in range(len(names)):
            if names[i] and id_cards[i]:
                distributions.append({
                    'villager_name': names[i],
                    'id_card': id_cards[i],
                    'amount': float(amounts[i]) if amounts[i] else subsidy.amount
                })
        if distributions:
            SubsidyService.distribute(subsidy_id, distributions)
            flash('补贴发放登记成功', 'success')
        return redirect(url_for('subsidies.detail', subsidy_id=subsidy_id))
    return render_template('subsidies/distribute.html', subsidy=subsidy)


@subsidies_bp.route('/<int:subsidy_id>/delete', methods=['POST'])
@login_required
def delete(subsidy_id):
    if SubsidyService.delete(subsidy_id):
        flash('补贴项目删除成功', 'success')
    else:
        flash('补贴项目删除失败', 'danger')
    return redirect(url_for('subsidies.list_subsidies'))


@subsidies_bp.route('/distribution/<int:dist_id>/confirm', methods=['POST'])
@login_required
def confirm_distribution(dist_id):
    result = SubsidyService.confirm_distribution(dist_id)
    if result:
        flash('补贴发放确认成功', 'success')
    else:
        flash('确认失败', 'danger')
    return redirect(url_for('subsidies.detail', subsidy_id=result.subsidy_id))
