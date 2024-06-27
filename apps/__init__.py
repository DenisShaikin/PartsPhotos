from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

from .api import blueprint


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PHOTOS_FILE = os.path.join(basedir, 'photos.csv')
    PHOTOS_FOLDER = os.path.join('assets', 'img')

def register_extensions(app):
    db.init_app(app)

def configure_database(app):
    # push context manually to app
    with app.app_context():
        db.create_all()
    #
    # @app.teardown_request
    # def shutdown_session(exception=None):
    #     db.session.remove()

def create_app():
    app = Flask(__name__)
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
    # app.register_blueprint(api_b)

    return app
