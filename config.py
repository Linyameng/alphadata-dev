# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello flask!'
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'yang.zhou <yang.zhou@example.com>'
    # SQLALCHEMY_POOL_SIZE = 20
    # SQLALCHEMY_POOL_RECYCLE = 3000
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass



class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev1.sqlite')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:howbuy1!@10.12.110.167:3306/flaskTrade?charset=utf8"
    SQLALCHEMY_BINDS = {
        'private': 'sqlite:///' + os.path.join(basedir, 'private-data.sqlite'),
    }


class TestingConfig(Config):
    TESTING = True
    sSQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:howbuy1!@10.12.110.167:3306/flaskTrade?charset=utf8"
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:howbuy1!@10.12.110.167:3306/flaskTrade?charset=utf8"
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pro-data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
