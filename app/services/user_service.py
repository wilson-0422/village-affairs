from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.user import User


class UserService:
    @staticmethod
    def create(username, password, real_name, role='villager', phone=None):
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            real_name=real_name,
            role=role,
            phone=phone
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def update(user_id, **kwargs):
        user = User.query.get(user_id)
        if not user:
            return None
        for key, value in kwargs.items():
            if hasattr(user, key) and key != 'password_hash':
                setattr(user, key, value)
        if 'password' in kwargs:
            user.password_hash = generate_password_hash(kwargs['password'])
        db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
