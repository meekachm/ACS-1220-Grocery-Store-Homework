from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from grocery_app.models import User, GroceryStore
from flask_bcrypt import bcrypt
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    address = StringField('Address', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Submit')

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    price = StringField('Price', validators=[DataRequired()])
    category = SelectField('Category', choices=[('fruit', 'Fruit'), ('vegetable', 'Vegetable'), ('dairy', 'Dairy')], validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[DataRequired(), URL()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query.all(), allow_blank=True)
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('No user with that username. Please try again.')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not bcrypt.check_password_hash(user.password, password.data):
            raise ValidationError('Password doesn\'t match. Please try again.')
