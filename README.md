# 乡村村务数字化系统

## 项目简介

乡村村务数字化系统是一个面向农村基层治理的信息化管理平台，旨在推动村务公开透明、提升基层治理效能。系统涵盖集体资产台账、土地流转登记、惠民补贴发放、村集体活动管理和村务公示存档等核心功能模块。

## 技术栈

- **后端**: Python 3.11, Flask 3.0, SQLAlchemy, SQLite
- **前端**: Jinja2 模板引擎, Bootstrap 5, 原生 JavaScript
- **认证**: Flask-Login
- **部署**: Docker

## 功能模块

### 1. 集体资产台账
- 资产信息的增删改查
- 资产分类管理（房屋、土地、设备、其他）
- 资产状态跟踪（在用、闲置、报废）
- 资产分类统计和状态统计

### 2. 土地流转登记
- 土地流转信息登记
- 流转类型管理（出租、转让、入股）
- 流转状态跟踪（待审批、已生效、已到期、已取消）
- 流转类型统计

### 3. 惠民补贴发放
- 补贴项目创建和管理
- 补贴发放名单登记
- 发放状态确认
- 补贴类别统计

### 4. 村集体活动
- 活动创建和信息管理
- 活动状态跟踪（筹备中、进行中、已结束）
- 近期活动展示
- 活动状态统计

### 5. 村务公示存档
- 公示信息发布和管理
- 公示分类（财务公示、政策通知、人事任免、其他）
- 公示状态管理（草稿、已发布、已下架）
- 公示类别统计

### 6. 数据仪表盘
- 各模块数据总览
- 资产分类和状态统计
- 土地流转类型统计
- 补贴类别统计
- 活动和公示统计

## 项目结构

```
repo/
├── app/
│   ├── __init__.py          # 应用工厂
│   ├── models/              # 数据模型
│   │   ├── user.py          # 用户模型
│   │   ├── asset.py         # 资产模型
│   │   ├── land_transfer.py # 土地流转模型
│   │   ├── subsidy.py       # 补贴模型
│   │   ├── activity.py      # 活动模型
│   │   └── notice.py        # 公示模型
│   ├── routes/              # 路由蓝图
│   │   ├── auth.py          # 认证路由
│   │   ├── assets.py        # 资产路由
│   │   ├── land_transfers.py# 土地流转路由
│   │   ├── subsidies.py     # 补贴路由
│   │   ├── activities.py    # 活动路由
│   │   ├── notices.py       # 公示路由
│   │   └── main.py          # 主页和仪表盘路由
│   ├── services/            # 业务逻辑层
│   │   ├── user_service.py
│   │   ├── asset_service.py
│   │   ├── land_transfer_service.py
│   │   ├── subsidy_service.py
│   │   ├── activity_service.py
│   │   └── notice_service.py
│   ├── templates/           # Jinja2 模板
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── partials/
│   │   ├── auth/
│   │   ├── assets/
│   │   ├── land_transfers/
│   │   ├── subsidies/
│   │   ├── activities/
│   │   ├── notices/
│   │   └── dashboard/
│   └── static/              # 静态资源
│       ├── css/style.css
│       └── js/main.js
├── app.py                   # 应用入口
├── config.py                # 配置文件
├── seed.py                  # 种子数据
└── requirements.txt         # 依赖列表
```

## 快速开始

### 本地运行

```bash
cd repo
pip install -r requirements.txt
python seed.py
python app.py
```

访问 http://localhost:5000 即可使用系统。

### Docker 部署

```bash
cd village-affairs
docker build -t village-affairs .
docker run -p 5000:5000 -p 2222:22 village-affairs
```

### 默认账号

| 用户名 | 密码 | 姓名 | 角色 |
|--------|------|------|------|
| admin | admin123 | 系统管理员 | 管理员 |
| zhangsan | zhang123 | 张三 | 村民 |
| lisi | li123 | 李四 | 村民 |
| wangwu | wang123 | 王五 | 村民 |

## 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| SECRET_KEY | Flask 密钥 | village-affairs-secret-key-2024 |
| DATABASE_URL | 数据库连接 | sqlite:///village.db |
| SSH_ENABLE | 是否启用 SSH | - |

## 许可证

MIT License
