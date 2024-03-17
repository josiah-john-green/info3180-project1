"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import PropertyForm
from app.models import Property
from app.utils import get_uploaded_images

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Josiah-John Green")

@app.route('/properties')
def properties():
    """Render the website's propery listing page."""
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    """Render the website's property creation page."""
    form = PropertyForm()

    if form.validate_on_submit():
        photo = form.photo.data  # Access the uploaded file
        filename = secure_filename(photo.filename)  # Secure the filename
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the photo to the designated folder

        property = Property(
            title=form.title.data,
            description=form.description.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            price=form.price.data,
            type=form.type.data,
            location=form.location.data,
            photo=filename  # Store the filename in the database
        )
        db.session.add(property)
        db.session.commit()
        
        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))
    else:
        flash_errors(form)

    return render_template('create.html', form=form)

@app.route('/uploads/<filename>')
def photo(filename):
    """Render the page for a specific property."""
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties/<int:propertyid>')
def view(propertyid):
    """Render the page for a specific property."""
    property = Property.query.get_or_404(propertyid)
    return render_template('view.html', property=property)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
