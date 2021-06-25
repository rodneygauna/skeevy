'''
    File name: models.py
    Author: Rodney Gauna
    Date created: 2021-06-24
'''


# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# ------------------------------------------------------------------------------
# Pet
# ------------------------------------------------------------------------------
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    createdate = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# ------------------------------------------------------------------------------
# User
# ------------------------------------------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    createdate = db.Column(db.DateTime(timezone=True), default=func.now())
    pets = db.relationship('Pet')
