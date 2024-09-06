from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    api = Api(app, title="URL Shortener")

    from .routes import url_bp
    api.add_namespace(url_bp, path="/url_shortener")

    return app
