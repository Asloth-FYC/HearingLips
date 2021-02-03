import os
from flask import Flask
from app.blueprints.project import project_bp
from app.blueprints.user import user_bp
from app.extensions import db, migrate, cors
from app.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('lips')
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_logging(app):
    pass


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(project_bp)