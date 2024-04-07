from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app import app, db
from app.forms import LoginForm, User, RegistrationForm
from urllib.parse import urlsplit


# When these decorators are invoked, it'll request the URLs and return the value back to the browser

@app.route('/')
@app.route('/index')
@login_required #Must add this decorator if you want to protect the page from users that aren't logged in
def index():
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: #If the user is autherized with the creditionals and then redirects them to a page
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data)) #This searches where the username from the from is located in the database
        if user is None or not user.check_password(form.password.data): #This check if the password that is now hashed was provided is valid (matches) to the database user info
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) #This will alllow the user to stay logged in (changes the user to current_user)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for(next_page)) #If the user is logged in, this is where they will be redirected
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)