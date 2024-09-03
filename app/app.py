from config import Config
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    api = Api(app, title="URL Shortener")

    from routes import url_bp
    api.add_namespace(url_bp, path="/url_shortener")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
