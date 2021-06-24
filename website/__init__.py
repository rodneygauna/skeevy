from flask import Flask


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

    return app
