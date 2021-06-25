'''
    File name: auth.py
    Author: Rodney Gauna
    Date created: 2021-06-24
'''


# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from flask import Blueprint, render_template, request, flash

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
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')

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

        # Validation logic for the submit form
        if len(email) < 4:
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
            # add user to db
            pass

    return render_template("signup.html")
