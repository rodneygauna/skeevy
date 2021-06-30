'''
    File name: views.py
    Author: Rodney Gauna
    Date created: 2021-06-24
'''

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Pet
from . import db


# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------
views = Blueprint('views', __name__)


# ------------------------------------------------------------------------------
# Routes
# ------------------------------------------------------------------------------
@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/pets', methods=['GET', 'POST'])
@login_required
def pets():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        print(dob)

        # Add new pet to database
        new_pet = Pet(name=name, dob=dob, user_id=current_user.id)
        db.session.add(new_pet)
        db.session.commit()
        flash(' Pet added!', category='success')

    return render_template("pets.html", user=current_user)
