import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://localhost/URLShortener')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
