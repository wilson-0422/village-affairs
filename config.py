import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'village-affairs-secret-key-2024')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///village.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
