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


def create_app():
    '''Initializes  the application using Flask'''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
