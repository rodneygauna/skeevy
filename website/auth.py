from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", methods=['GET', 'POST'])


@auth.route('/logout')
def logout():
    return render_template("/")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash(' Email must be greater than 3 characters', category='error')

        elif len(firstname) <2:
            flash(' First name must be greater than 1 characters',
                  category='error')

        elif len(lastname) <2:
            flash(' Last name must be greater than 1 characters',
                  category='error')

        elif password1 != password2:
            flash(' Passwords don\'t match.', category='error')

        elif len(password1) <1:
            flash(' Password must be greater than 1 character',
                  category='error')

        else:
            # add user to db
            pass

    return render_template("signup.html")
