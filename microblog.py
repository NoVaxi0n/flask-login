import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post


#This is options used in the flask shell to load for testing purposes
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}