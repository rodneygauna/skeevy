"""Pets > Forms"""

# Imports
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    DateField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


# Form > Add Pet
class AddEditPetForm(FlaskForm):
    """Add/Edit Pet form"""

    required = DataRequired()
    name_length = Length(min=2, max=255)

    name = StringField(
        'Name (required)',
        validators=[required, name_length]
    )
    date_of_birth = DateField(
        'Date of Birth (required)',
        validators=[required]
    )
    gender = SelectField(
        'Gender (required)',
        choices=[
            ('', ''),
            ('male', 'Male'),
            ('female', 'Female'),
            ('unknown', 'Unknown'),
        ],
        validators=[required]
    )
    pet_type = SelectField(
        'Type (required)',
        choices=[
            ('', ''),
            ('dog', 'Dog'),
            ('cat', 'Cat'),
            ('other', 'Other'),
        ],
        validators=[required]
    )
    breed = StringField(
        'Breed (required)',
        validators=[required, name_length]
    )
    submit = SubmitField('Submit')
