from flask import render_template
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Riley' }
    posts = [
        {
            'author': { 'nickname': 'James' },
            'body': "Mah name's James!"
        },
        {
            'author': { 'nickname': 'Angie' },
            'body': "I'm Angie ^^"
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)
