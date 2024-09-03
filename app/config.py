import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///urls.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
