# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app
from . import login_manager
from . import db
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class AnonymousUser(AnonymousUserMixin):

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=True, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderate': (Permission.FOLLOW |
                         Permission.COMMENT |
                         Permission.WRITE_ARTICLES |
                         Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions, role.default = roles.get(r)
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)

    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expires=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expires=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_change_email_token(self, new_email, expires=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({'user_id': self.id, 'email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('user_id') != self.id:
            return False
        new_email = data.get('email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User %r>' % self.username


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


class PageView(db.Model):
    __tablename__ = 'pageview'
    id = db.Column(db.Integer, primary_key=True)
    view = db.Column(db.String(64), index=True)
    pv = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime(), default=datetime.utcnow)
    last_time = db.Column(db.DateTime(), default=datetime.utcnow)

    def update_time(self):
        self.last_time = datetime.utcnow()
        db.session.add(self)


class EnvironMapping(db.Model):
    __tablename__ = 'environ_mapping'
    id = db.Column(db.Integer, primary_key=True)
    tp_ip = db.Column(db.String(64))
    tms_ip = db.Column(db.String(64), index=True)
    user_prefix = db.Column(db.String(64))
    tms_db = db.Column(db.String(64), default='192.168.220.119')
    tp_db = db.Column(db.String(64), default='192.168.220.126')
    tms_dsn = db.Column(db.String(64), default='192.168.220.119:1521/hbqa')
    tp_dsn = db.Column(db.String(64), default='192.168.220.126:1521/hbqa11g')
    db_password = db.Column(db.String(64), default='howbuy2015')
    redis_peer = db.Column(db.String(64))

class SaveSql(db.Model):
    __tablename__ = 'save_sql'
    id = db.Column(db.Integer, primary_key=True)
    SQL_statements = db.Column(db.String(64))
    instance = db.Column(db.String(64))
    Desc = db.Column(db.String(250))
    creator = db.Column(db.String(64))
    modifier = db.Column(db.String(64))
    CREATE_DATE = db.Column(db.Date)
    UPDATE_DATE = db.Column(db.Date)

class actioncolumn(db.Model):
    __tablename__ = 'actioncolumn'
    actioncolumnid = db.Column(db.Integer, primary_key=True)
    actioncolumnname = db.Column(db.String(255))
