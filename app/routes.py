# Defines the routes for your application, handling URL mappings to Python functions, and includes authentication and form handling logic.
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, User, RegistrationForm
from urllib.parse import urlsplit

# Route for the home page, requires user to be logged in
# When these decorators are invoked, it'll request the URLs and return the value back to the browser
@app.route('/')
@app.route('/index')
@login_required # Must add this decorator if you want to protect the page from users that aren't logged in
def index():
    # Mockup data for posts to display on the home page
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


# Login URL that creates a form, and passes it to the templete for rendering
# form=form creates the form fields to render
# GET grabs the user input and sends it to the server
# POST receives GET input and tells what to return

# Simplified: Route for handling login, allows GET to display the form and POST to process it
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Redirect authenticated users to the home page
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Query the database for the user by username
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data)) 
        # Validate user and password
        if user is None or not user.check_password(form.password.data): 
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #This will alllow the user to stay logged in (changes the user to current_user)
        login_user(user, remember=form.remember_me.data) 
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
            #If the user is logged in, this is where they will be redirected
        return redirect(url_for(next_page)) 
    return render_template('login.html', title='Sign In', form=form)

# Route to log out a user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Route for handling registration, supports GET for form display and POST for processing
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Creates a new user and add to the database
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)