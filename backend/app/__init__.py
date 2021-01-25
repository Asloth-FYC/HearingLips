from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
from app.user.view import user_bp

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(user_bp)
    db.init_app(app)
    Migrate(app, db)
    return app
