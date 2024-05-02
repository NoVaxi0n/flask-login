# Manages form creation and validation, ensuring user input is processed securely and effectively.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

# validators = Checks if the field is not submitted empty

# Define LoginForm using FlaskForm, providing fields for user login
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')  # Option to remember the user login
    submit = SubmitField('Sign In') # Submit button for the form

# Define RegistrationForm for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    # These methods will be automatically called by Flask-wtf when a form is being processed
    # db.session.scaler is a query call where it checks if the user exists, or None if it doesnt

    # Custom validation method to ensure username uniqueness
    def validate_username(self, username):
         # Query the database to check if username is already taken
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    # Custom validation method to ensure email uniqueness
    def validate_email(self, email):
        # Query the database to check if email is already registered
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')