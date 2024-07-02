
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config


db = SQLAlchemy()
from .api import blueprint

def register_extensions(app):
    db.init_app(app)
    # csrf = CSRFProtect()
    # csrf.init_app(app)
    return

def configure_database(app):
    # @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


# def init_tireDiameters(diamList, session):

def create_app(config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(Config)
    register_extensions(app)
    configure_database(app)

    CORS(app)
    # db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization,x-api-key"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,OPTION,PUT,POST,DELETE"
        )
        return response

    app.register_blueprint(blueprint)
    return app


