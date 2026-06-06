from app import create_app, db
from app.models.user import User
from app.models.asset import Asset
from app.models.land_transfer import LandTransfer
from app.models.subsidy import Subsidy, SubsidyDistribution
from app.models.activity import Activity
from app.models.notice import Notice
from app.services.user_service import UserService
from datetime import date, datetime

app = create_app()

with app.app_context():
    db.create_all()

    if User.query.first() is None:
        UserService.create('admin', 'admin123', '系统管理员', 'admin', '13800000001')
        UserService.create('zhangsan', 'zhang123', '张三', 'villager', '13800000002')
        UserService.create('lisi', 'li123', '李四', 'villager', '13800000003')
        UserService.create('wangwu', 'wang123', '王五', 'villager', '13800000004')
        UserService.create('zhaoliu', 'zhao123', '赵六', 'villager', '13800000005')
        UserService.create('sunqi', 'sun123', '孙七', 'villager', '13800000006')

    if Asset.query.first() is None:
        assets_data = [
            {'name': '村委会办公楼', 'category': '房屋', 'value': 500000, 'quantity': 1, 'location': '村中心路1号', 'status': '在用', 'description': '三层砖混结构，建筑面积600平方米，2008年建成'},
            {'name': '集体农用机械', 'category': '设备', 'value': 120000, 'quantity': 5, 'location': '村农机站', 'status': '在用', 'description': '包含拖拉机3台、收割机2台'},
            {'name': '村文化广场', 'category': '房屋', 'value': 300000, 'quantity': 1, 'location': '村中心', 'status': '在用', 'description': '占地面积2000平方米，含舞台和健身设施'},
            {'name': '废弃仓库', 'category': '房屋', 'value': 80000, 'quantity': 1, 'location': '村东头', 'status': '闲置', 'description': '砖木结构，建于1995年，需修缮'},
            {'name': '集体耕地（东片）', 'category': '土地', 'value': 200000, 'quantity': 1, 'location': '村东片区', 'status': '在用', 'description': '面积约100亩，水浇地'},
            {'name': '集体耕地（南片）', 'category': '土地', 'value': 150000, 'quantity': 1, 'location': '村南片区', 'status': '在用', 'description': '面积约80亩，旱地'},
            {'name': '灌溉水渠', 'category': '其他', 'value': 60000, 'quantity': 1, 'location': '全村范围', 'status': '在用', 'description': '主渠3公里，支渠5公里'},
            {'name': '旧村委会用房', 'category': '房屋', 'value': 45000, 'quantity': 1, 'location': '村西头', 'status': '报废', 'description': '建于1980年，已列为危房'},
        ]
        for data in assets_data:
            asset = Asset(**data)
            db.session.add(asset)
        db.session.commit()

    if LandTransfer.query.first() is None:
        transfers_data = [
            {'land_location': '东片区50亩', 'area': 50, 'transfer_type': '出租', 'from_party': '村集体', 'to_party': '李四', 'price': 50000, 'start_date': date(2024, 3, 1), 'end_date': date(2029, 2, 28), 'status': '已生效', 'description': '用于种植水稻，租金每年1000元/亩'},
            {'land_location': '南片区30亩', 'area': 30, 'transfer_type': '入股', 'from_party': '王五', 'to_party': '村集体合作社', 'price': 30000, 'start_date': date(2024, 6, 1), 'end_date': date(2034, 5, 31), 'status': '已生效', 'description': '以土地入股村合作社，享受分红'},
            {'land_location': '西片区20亩', 'area': 20, 'transfer_type': '转让', 'from_party': '赵六', 'to_party': '孙七', 'price': 40000, 'start_date': date(2024, 1, 1), 'end_date': date(2043, 12, 31), 'status': '已生效', 'description': '土地经营权转让，用于果树种植'},
            {'land_location': '北片区15亩', 'area': 15, 'transfer_type': '出租', 'from_party': '村集体', 'to_party': '张三', 'price': 18000, 'start_date': date(2025, 1, 1), 'end_date': date(2027, 12, 31), 'status': '待审批', 'description': '拟用于蔬菜大棚建设'},
            {'land_location': '东片区10亩', 'area': 10, 'transfer_type': '出租', 'from_party': '村集体', 'to_party': '周八', 'price': 12000, 'start_date': date(2022, 1, 1), 'end_date': date(2024, 12, 31), 'status': '已到期', 'description': '用于小麦种植，合同已到期'},
        ]
        for data in transfers_data:
            transfer = LandTransfer(**data)
            db.session.add(transfer)
        db.session.commit()

    if Subsidy.query.first() is None:
        subsidy1 = Subsidy(name='农业支持保护补贴', category='农业补贴', amount=150, total_budget=150000, description='对种地农民的直补，每亩补贴150元')
        db.session.add(subsidy1)
        db.session.commit()

        dists1 = [
            SubsidyDistribution(subsidy_id=subsidy1.id, villager_name='张三', id_card='320123199001011234', amount=1500, status='已发放', distributed_at=datetime(2024, 6, 15)),
            SubsidyDistribution(subsidy_id=subsidy1.id, villager_name='李四', id_card='320123199202022345', amount=7500, status='已发放', distributed_at=datetime(2024, 6, 15)),
            SubsidyDistribution(subsidy_id=subsidy1.id, villager_name='王五', id_card='320123199303033456', amount=4500, status='待发放'),
        ]
        for d in dists1:
            db.session.add(d)
        db.session.commit()

        subsidy2 = Subsidy(name='义务教育阶段补贴', category='教育补贴', amount=500, total_budget=50000, description='义务教育阶段学生每学期500元补贴')
        db.session.add(subsidy2)
        db.session.commit()

        dists2 = [
            SubsidyDistribution(subsidy_id=subsidy2.id, villager_name='张三', id_card='320123199001011234', amount=500, status='已发放', distributed_at=datetime(2024, 9, 1)),
            SubsidyDistribution(subsidy_id=subsidy2.id, villager_name='赵六', id_card='320123199505055678', amount=500, status='待发放'),
        ]
        for d in dists2:
            db.session.add(d)
        db.session.commit()

        subsidy3 = Subsidy(name='新型农村合作医疗补贴', category='医疗补贴', amount=200, total_budget=100000, description='新农合参保补贴，每人每年200元')
        db.session.add(subsidy3)
        db.session.commit()

        subsidy4 = Subsidy(name='农村养老保险补贴', category='养老补贴', amount=300, total_budget=120000, description='60岁以上老人每月补贴300元')
        db.session.add(subsidy4)
        db.session.commit()

    if Activity.query.first() is None:
        activities_data = [
            {'title': '春节联欢晚会', 'content': '全村春节联欢活动，包含文艺表演、抽奖等环节，欢迎全体村民参加。', 'activity_date': date(2024, 2, 9), 'location': '村文化广场', 'organizer': '村委会', 'participants_count': 350, 'status': '已结束'},
            {'title': '植树节义务植树活动', 'content': '组织村民在村道两旁和荒山进行义务植树，美化村容村貌。', 'activity_date': date(2024, 3, 12), 'location': '村道及后山', 'organizer': '村委会', 'participants_count': 120, 'status': '已结束'},
            {'title': '乡村振兴座谈会', 'content': '邀请专家和村民代表共同探讨乡村振兴发展路径，集思广益。', 'activity_date': date(2024, 8, 15), 'location': '村委会会议室', 'organizer': '村委会', 'participants_count': 45, 'status': '进行中'},
            {'title': '夏季防汛演练', 'content': '组织防汛应急演练，提高村民防灾减灾意识和应急处置能力。', 'activity_date': date(2024, 7, 20), 'location': '村河堤', 'organizer': '村委会', 'participants_count': 0, 'status': '筹备中'},
            {'title': '中秋文艺汇演', 'content': '中秋节文艺汇演，包含歌舞、小品、戏曲等节目。', 'activity_date': date(2024, 9, 17), 'location': '村文化广场', 'organizer': '村委会', 'participants_count': 200, 'status': '已结束'},
        ]
        for data in activities_data:
            activity = Activity(**data)
            db.session.add(activity)
        db.session.commit()

    if Notice.query.first() is None:
        notices_data = [
            {'title': '2024年度财务收支公示', 'content': '根据《村民委员会组织法》和村务公开制度的要求，现将2024年度村级财务收支情况公示如下：\n\n一、收入情况\n1. 上级转移支付：85,000元\n2. 集体经营收入：42,000元\n3. 土地流转收入：50,000元\n4. 其他收入：8,000元\n合计：185,000元\n\n二、支出情况\n1. 办公经费：12,000元\n2. 公共设施维护：35,000元\n3. 文体活动支出：15,000元\n4. 困难群众慰问：8,000元\n5. 其他支出：10,000元\n合计：80,000元\n\n三、结余情况\n本年度结余：105,000元\n\n公示期：2024年12月1日至12月15日\n如有异议，请到村委会反映。', 'category': '财务公示', 'publisher': '村委会', 'publish_date': date(2024, 12, 1), 'status': '已发布'},
            {'title': '关于开展农村人居环境整治的通知', 'content': '各位村民：\n\n为改善村容村貌，提升人居环境质量，经村委会研究决定，在全村范围内开展人居环境整治行动。\n\n一、整治时间：2024年6月1日至6月30日\n二、整治内容：\n1. 清理房前屋后杂物\n2. 整治乱搭乱建\n3. 清理沟渠垃圾\n4. 美化庭院环境\n\n请各位村民积极配合，共同建设美丽家园。', 'category': '政策通知', 'publisher': '村委会', 'publish_date': date(2024, 5, 25), 'status': '已发布'},
            {'title': '村委会成员调整公告', 'content': '经村民代表大会选举通过，现将村委会成员调整情况公告如下：\n\n主任：王建国\n副主任：李明\n委员：张秀英、赵德才、孙丽华\n\n以上人员自公告之日起履职。', 'category': '人事任免', 'publisher': '村委会', 'publish_date': date(2024, 4, 10), 'status': '已发布'},
            {'title': '夏季防溺水安全提示', 'content': '夏季来临，为防止溺水事故发生，特提醒广大村民：\n\n1. 严禁未成年人在无成人陪同下到河边、池塘等水域游泳\n2. 家长要加强对未成年人的看护\n3. 发现溺水事故及时拨打110和120\n\n珍爱生命，远离危险水域！', 'category': '政策通知', 'publisher': '村委会', 'publish_date': None, 'status': '草稿'},
            {'title': '2024年第二季度财务收支公示', 'content': '2024年第二季度村级财务收支情况公示。', 'category': '财务公示', 'publisher': '村委会', 'publish_date': date(2024, 7, 5), 'status': '已发布'},
        ]
        for data in notices_data:
            notice = Notice(**data)
            db.session.add(notice)
        db.session.commit()

    print('种子数据初始化完成！')
