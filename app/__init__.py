# Initializes the Flask application, binding together configurations, database setup, and login management.

# Importing necessary modules and classes for the Flask application setup
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Create a Flask application instance
app = Flask(__name__)
# Load configuration from the Config class defined in config.py
app.config.from_object(Config)
# Initialize SQLAlchemy for database interactions
db = SQLAlchemy(app)
# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)
# Initialize Flask-Login for managing user sessions
login = LoginManager(app)
# Define the default view for login, used by Flask-Login for unauthorized access to protected views
login.login_view = 'login' 

# Import routes and models modules to ensure they are part of the app context
from app import routes, models
