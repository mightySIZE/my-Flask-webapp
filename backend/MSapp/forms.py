from flask_wtf import FlaskForm
from MSapp.models import User
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError

#>>> python
#>>> import os
#>>> os.urandom(12).hex()
#'<secret key generated by os.urandom()>'
# this is the secret key for the form
class RegisterationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Sign Up') 

    def validate_username(self, username_to_check): # this function will check if the username already exists in the database, validate is a special function name in flask_wtf module. validate_'username' is the parameter that will be passed to the function
        user = User.query.filter_by(username=username_to_check.data).first() # this line will query the database to see if the username already exists
        if user:
            raise ValidationError('Username already exists. Please choose a different username.')
        
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first() #first retrieves the first case of the email in the database
        if email:
            raise ValidationError('Email already exists. Please choose a different email.')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    searchName = StringField('Search Name', validators=[DataRequired()])
    submit = SubmitField('Search')