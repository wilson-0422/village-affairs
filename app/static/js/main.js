document.addEventListener('DOMContentLoaded', function () {
    var addRowBtn = document.getElementById('addRow');
    if (addRowBtn) {
        addRowBtn.addEventListener('click', function () {
            var list = document.getElementById('distributionList');
            var row = document.createElement('div');
            row.className = 'row mb-2 distribution-row';
            row.innerHTML = '<div class="col-md-4"><input type="text" class="form-control" name="villager_name" placeholder="村民姓名" required></div>' +
                '<div class="col-md-4"><input type="text" class="form-control" name="id_card" placeholder="身份证号" required></div>' +
                '<div class="col-md-3"><input type="number" class="form-control" name="amount" step="0.01" placeholder="发放金额"></div>' +
                '<div class="col-md-1"><button type="button" class="btn btn-outline-danger btn-sm remove-row" title="删除">✕</button></div>';
            list.appendChild(row);
        });
    }

    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('remove-row')) {
            var row = e.target.closest('.distribution-row');
            var list = document.getElementById('distributionList');
            if (list.children.length > 1) {
                row.remove();
            }
        }
    });

    var alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
