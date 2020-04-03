import datetime
import json

from flask_login import UserMixin, current_user
from sqlalchemy import event, inspect
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.attributes import get_history
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

ACTION_CREATE = 1
ACTION_UPDATE = 2
ACTION_DELETE = 3

class Base(db.Model):
    """Base model class to implement db columns and features every model should have"""
    __abstract__ = True

    def __tablename__(cls):
        return cls.__name__.lower()

    id = db.Column(db.Integer, primary_key=True, nullable=False)

class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True} 
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128), index=False, unique=False)
    user_name = db.Column(db.String(120), index=False, unique=False)
    phone = db.Column(db.String(120), index=False, unique=False)
    reset_code = db.Column(db.String(10), index=False, unique=False)
    verified = db.Column(db.String(10), index=False, unique=False)
    verification_code = db.Column(db.String(10), index=False, unique=False)
    is_admin = db.Column(db.String(10), index=False, unique=False)
    is_banned = db.Column(db.String(5), index=False, unique=False)
    is_funny = db.Column(db.String(5), index=False, unique=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def get_id(self):
        try:
            return unicode(self.user_id)
        except NameError:
            return str(self.user_id)

    def __repr__(self):
            return '<User %r>' % (self.id)