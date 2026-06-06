from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = '请先登录'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.assets import assets_bp
    from app.routes.land_transfers import land_transfers_bp
    from app.routes.subsidies import subsidies_bp
    from app.routes.activities import activities_bp
    from app.routes.notices import notices_bp
    from app.routes.main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(land_transfers_bp)
    app.register_blueprint(subsidies_bp)
    app.register_blueprint(activities_bp)
    app.register_blueprint(notices_bp)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))
