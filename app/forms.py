from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    
    bedrooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    
    price = IntegerField('Price', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])

    location = StringField('Location', validators=[DataRequired()], render_kw={"class": "tyoe-select"})
    
    photo = FileField('Photo')