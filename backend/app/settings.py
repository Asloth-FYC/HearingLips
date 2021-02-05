import os

# 项目根目录
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='LAAT4AM12'
    MAIL_SERVER='smtp.qq.com'
    MAIL_PORT=25
    MAIL_USE_TLS=True
    MAIL_PASSWORD='ocypqlqiodrcbafb'
    MAIL_USERNAME='1154205999@qq.com'
    MAIL_DEFAULT_SENDER='1154205999@qq.com'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:594666@localhost/flask_study'


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:594666@127.0.0.1:3306/flask_study'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
