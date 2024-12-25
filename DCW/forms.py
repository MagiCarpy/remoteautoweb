from flask_wtf import FlaskForm
from DCW.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError, Regexp

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Enter Username"),
                                                   Length(min=2, max=20),
                                                   Regexp("^(?=.{1,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")])
    email = StringField('Email', validators = [InputRequired("Enter Email"), Email()])
    password = PasswordField('Password', validators=[InputRequired("Enter Password")])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired("Confirm Password"),
                                                                    EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        
        if user:
            raise ValidationError('Username Already In Use')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        
        if user:
            raise ValidationError('Email Already In Use')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired("Enter Username"),
                                                   Length(min=2, max=20),
                                                   Regexp("^(?=.{1,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$")])
    password = PasswordField('Password', validators=[InputRequired("Enter Password")])
    submit = SubmitField('Login')