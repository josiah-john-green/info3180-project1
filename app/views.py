"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from app import app, db, mail
from app.forms import PropertyForm, ContactForm  
from app.models import Property
from flask_mail import Message

# Render website's home page
@app.route('/')
def home():
    return render_template('home.html')

# Render the website's about page
@app.route('/about/')
def about():
    return render_template('about.html', name="Josiah-John Green")

# Render the website's property listing page
@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

# Render the website's property creation page
@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    form = PropertyForm()

    if form.validate_on_submit():
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        property = Property(
            title=form.title.data,
            description=form.description.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            price=form.price.data,
            type=form.type.data,
            location=form.location.data,
            photo=filename
        )
        db.session.add(property)
        db.session.commit()
        
        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))
    else:
        flash_errors(form)

    return render_template('create.html', form=form)

# Serve uploaded photos
@app.route('/uploads/<filename>')
def photo(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

# Render the page for a specific property
@app.route('/properties/<int:propertyid>')
def view(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('view.html', property=property, propertyid=propertyid)


# Process and send email
@app.route('/email/<int:propertyid>', methods=['GET', 'POST'])
def email(propertyid):
    form = ContactForm()
    property = Property.query.get_or_404(propertyid)

    if form.validate_on_submit():
        try:
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data

            msg = Message(subject, sender=(name, email), recipients=["to@example.com"])
            msg.body = f"From: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}"
            mail.send(msg)

            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('properties'))

        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('email.html', form=form, property=property)  # Pass the 'property' variable to the template

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

# Additional routes and error handling

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


