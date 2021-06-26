'''
    File name: __init__.py
    Author: Rodney Gauna
    Date created: 2021-06-24
'''

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# ------------------------------------------------------------------------------
# Database Global Variables
# ------------------------------------------------------------------------------
db = SQLAlchemy()
DB_NAME = 'database.db'


# ------------------------------------------------------------------------------
# Read Secret Key from the secretkey.txt file
# ------------------------------------------------------------------------------
def read_secret_key():
    '''Open text file, read the secret key and returns it'''
    with open("secretkey.txt", "r") as r:
        lines = r.readlines()
        return lines[0].strip()


secret_key = read_secret_key()


# ------------------------------------------------------------------------------
# Application initialization
# ------------------------------------------------------------------------------
def create_app():
    '''Initializes  the application using Flask'''
    app = Flask(__name__)
    # Flask secret key configuration
    app.config['SECRET_KEY'] = secret_key
    # Flask and SQLAlchemy database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import views and auth routes
    from .views import views
    from .auth import auth

    # Blueprint routing
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Check if database exists; if not, create database and tables (as classes)
    from .models import User, Pet
    create_database(app)

    # Initializes the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# ------------------------------------------------------------------------------
# Database initialization
# ------------------------------------------------------------------------------
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')
