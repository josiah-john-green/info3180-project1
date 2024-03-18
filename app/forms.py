from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email

class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    
    bedrooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    
    price = StringField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])

    location = StringField('Location', validators=[DataRequired()])
    
    photo = FileField('Photo')

class ContactForm(FlaskForm):
    
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])