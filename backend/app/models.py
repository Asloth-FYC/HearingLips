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
    filepath = db.Column(db.String(40), nullable=False)
    create_at = db.Column(db.DateTime,default=datetime.datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))