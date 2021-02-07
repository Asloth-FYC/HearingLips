import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

from app.blueprints.email import email_bp
from app.blueprints.project import project_bp
from app.blueprints.user import user_bp
from app.extensions import db, migrate, cors, mail
from app.settings import config, basedir


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG')

    app = Flask('lips')
    app.config.from_object(config[config_name])

    app.config.update(
        MAIL_PORT=465,
        MAIL_USE_SSL = True
    )

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)

    return app


def register_logging(app):
    app.logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s  -  %(name)s  -  %(levelname)s  -  %(massage)s')
    file_handler = RotatingFileHandler(basedir + '/logs/backend.log', maxBytes=10 * 1024 * 1024, backupCount=10)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    if not app.debug:
        app.logger.addHandler(file_handler)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    mail.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(email_bp)
