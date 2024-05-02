# Sets up the database models using SQLAlchemy, detailing user and post models, which are crucial for data handling and relationships.
from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

# UserMixin provides additional functions that can be used for user verification
# so.Mapped[int] or so.Mapped[str] defines the type of the column used in the database, forcing values to be required

# User model definition using SQLAlchemy ORM and Flask-Login for easier user session management
class User(UserMixin, db.Model):
    # Define columns with data types and constraints
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    # Relationship to the Post model, linked by the 'author' field in Post
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    # Representation method for the User instance
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # Set password method hashes the password and stores it
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password method validates a given password against the stored hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Function to load user by ID for Flask-Login integration
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

# Post model definition, representing blog posts
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id),index=True)
    # Relationship to the User model, linked by the 'posts' field in User
    author: so.Mapped[User] = so.relationship(back_populates='posts')
    
    # Representation method for the Post instance
    def __repr__(self):
        return '<Post {}>'.format(self.body)