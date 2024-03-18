from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate here
from flask_mail import Mail 
from app.config import Config

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Mail here
mail = Mail(app) 

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

# Import views after initializing dependencies
from app import views