"""Pets > Views"""

# Imports
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    login_required,
    current_user,
)
from src import db
from .forms import (
    AddEditPetForm,
)
from .models import (
    Pet,
    UserPet,
)


# Blueprint Configuration
pets_bp = Blueprint('pets', __name__)


# Pets > Add new pet
@login_required
@pets_bp.route('/pets/add', methods=['GET', 'POST'])
def add_pet():
    """"Add a new pet"""

    form = AddEditPetForm()

    if form.validate_on_submit():
        pet_data = {
            field.name: getattr(form, field.name).data
            for field in form
            if field.name not in ('csrf_token', 'submit')
        }
        pet_data.update({
            'created_by': current_user.id
        })
        new_pet = Pet(**pet_data)
        db.session.add(new_pet)
        db.session.commit()

        user_pet = UserPet(
            relationship_type='owner',
            user_id=current_user.id,
            pet_id=new_pet.id,
        )
        db.session.add(user_pet)
        db.session.commit()

        flash('Pet added successfully!', 'success')
        return redirect(url_for('pets.list_pets'))

    return render_template('pets/add_edit.html',
                           title='Skeevy - Add Pet',
                           form=form)


# Pets > Edit pet
@login_required
@pets_bp.route('/pets/edit/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit a pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddEditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        pet.updated_by = current_user.id
        pet.updated_date = datetime.utcnow()
        db.session.commit()

        flash('Pet updated successfully!', 'success')
        return redirect(url_for('pets.list_pets'))

    return render_template('pets/add_edit.html',
                           title='Skeevy - Edit Pet',
                           form=form)


# Pets > View List of Pets
@login_required
@pets_bp.route('/pets', methods=['GET'])
def list_pets():
    """List all pets"""

    pets = (
        db.session.query(Pet)
        .filter(UserPet.user_id == current_user.id)
    )

    return render_template('pets/list.html',
                           title='Skeevy - Pets',
                           pets=pets)
