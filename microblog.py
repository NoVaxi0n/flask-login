 # Initializes the shell context for Flask, making it easier to interact with the application components during development.

# Importing sqlalchemy modules for database operations
import sqlalchemy as sa
import sqlalchemy.orm as so

from app import app, db
from app.models import User, Post


# Decorator to setup a shell context for Flask application; makes these items available in flask shell
# Used for testing purposes
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}