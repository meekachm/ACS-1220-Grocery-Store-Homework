from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

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
