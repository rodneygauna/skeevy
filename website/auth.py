'''
    File name: auth.py
    Author: Rodney Gauna
    Date created: 2021-06-24
'''


# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------
auth = Blueprint('auth', __name__)


# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    '''Login page'''
    # Gets the data from the form and saves as variables
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Checks if the user's email is on file
        user = User.query.filter_by(email=email).first()
        # Checks if the password is correct
        if user:
                if check_password_hash(user.password, password):
                    flash(' Logged in successfully!', category='success')
                else:
                    flash(' Incorrect password, try again.', category='error')
        else:
            flash(' Account not found. Check if email is correct and try again.',
                  category='error')

    return render_template("login.html")


@auth.route('/logout')
def logout():
    '''Logout page'''
    return render_template("/")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    '''Sign up page'''
    # Gets the data from the form and saves as variables
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checks if email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash(' Email is already in use.', category='error')    # security issue - should look at some better wording
        # Validation logic for the submit form
        elif len(email) < 4:
            flash(' Email must be greater than 3 characters', category='error')
        elif len(firstname) < 2:
            flash(' First name must be greater than 1 characters',
                  category='error')
        elif len(lastname) < 2:
            flash(' Last name must be greater than 1 characters',
                  category='error')
        elif password1 != password2:
            flash(' Passwords don\'t match.', category='error')
        elif len(password1) < 1:
            flash(' Password must be greater than 1 character',
                  category='error')
        else:
            # Add new user to database
            new_user = User(email=email, firstname=firstname,
                            lastname=lastname,
                            password=generate_password_hash(password1,
                                                            method='sha384'))
            db.session.add(new_user)
            db.session.commit()
            flash(' Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html")
