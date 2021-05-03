import datetime
from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    projects = db.relationship('Project')


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.String(40), default=str(datetime.date.today()))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
