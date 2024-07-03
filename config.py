# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

import os
from decouple import config


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PHOTOS_FILE = os.path.join(basedir, 'photos.csv')
    PHOTOS_FOLDER = os.path.join('assets', 'img')

    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_008')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    DOMAIN_NAME = 'http:\/\/frankserv.ru\/'
    DOMAIN_NAME_ = 'http:\\\\frankserv.ru'
    BASEDIR_ = basedir

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['chaikide@mail.ru']
 
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

class ProductionConfig(Config):
    DEBUG = False
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
    # PostgreSQL database
    # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    #     config( 'DB_ENGINE'   , default='postgresql'    ),
    #     config( 'DB_USERNAME' , default='appseed'       ),
    #     config( 'DB_PASS'     , default='pass'          ),
    #     config( 'DB_HOST'     , default='localhost'     ),
    #     config( 'DB_PORT'     , default=5432            ),
    #     config( 'DB_NAME'     , default='appseed-flask' )
    # MySQL database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if os.getenv('FLASK_ENV')=='Production':
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        # CELERY_BROKER_URL = 'redis://redis:6379/0'
        # CELERY_RESULT_BACKEND = 'redis://redis:6379/0'


class DebugConfig(Config):
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
