from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
