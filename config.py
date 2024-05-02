# Holds the configuration settings for the Flask app, such as database connections and secret keys, prioritizing security and scalability.

import os

# Storing the absolute path of the current file's directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Setting the secret key for cryptographic components, fetching from environment variable or setting default
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Configuring the SQLALCHEMY_DATABASE_URI for connection to the database, fetching from environment or default to SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')