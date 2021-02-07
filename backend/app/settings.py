import os

# 项目根目录
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


dotenv_path = os.path.join(os.getcwd(), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=os.getenv('SECRET_KEY')
    MAIL_SERVER=os.getenv('MAIL_SERVER')
    MAIL_USE_TLS=os.getenv('MAIL_USE_TLS')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_DEFAULT_SENDER')


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_Dev')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI_Pro')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
