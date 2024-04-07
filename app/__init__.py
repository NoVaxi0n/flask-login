#Creates application object as an instance
#Creates Database setup
#Creates a Login Management

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' #If user is not signed in, this will automatically force user to login if they try to view a protected page

#Routes handles URLs, Models defines the structure of the database
from app import routes, models
