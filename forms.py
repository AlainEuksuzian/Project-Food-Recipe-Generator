from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired



# The Login class is a FlaskForm that contains fields for username, password, remember me checkbox,
# and a login button.
class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    login_btn = SubmitField('Sign In')


# The Signup class is a FlaskForm that contains fields for first name, last name, email, username,
# password, gender, and a submit button.

class Signup(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('Male','Male'), ('Female', 'Female')])
    sign_btn = SubmitField('Sign In')